from django.shortcuts import render, redirect, get_object_or_404
from .forms import TokoEntryForm, ProductEntryForm
from .models import TokoEntry, ProductEntry
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.core.exceptions import ValidationError
import re
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import viewsets
from .serializer import TokoEntrySerializer, ProductEntrySerializer
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.views import APIView

def show_main(request):
    toko_entries = TokoEntry.objects.all()
    product_entries = ProductEntry.objects.all()

    unique_locations = set(toko_entry.location.lower() for toko_entry in toko_entries)
    unique_locations_display = {location: toko_entry.location for toko_entry in toko_entries for location in unique_locations if location == toko_entry.location.lower()}

    
    context = {
        'toko_entries': toko_entries,
        'product_entries': product_entries,
        'unique_locations': unique_locations_display.values(),
    }

    return render(request, "boardadmin.html", context)

def create_toko_entry(request):
    form = TokoEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect ('dashboard_admin:show_main')
    
    context = {'form': form}
    return render(request, "create_toko_entry.html", context)

def create_product_entry(request):
    if request.method == "POST":
        form = ProductEntryForm(request.POST, request.FILES)  
        if form.is_valid():
            try:
                form.save()
                return redirect('dashboard_admin:show_main')
            except ValidationError as e:
                form.add_error('name', e)
    else:
        form = ProductEntryForm()

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    toko_data = serializers.serialize("xml", TokoEntry.objects.all())
    product_data = serializers.serialize("xml", ProductEntry.objects.all())

    # Menghapus deklarasi XML <?xml ... ?> dari kedua hasil serialisasi
    toko_data = re.sub(r'<\?xml[^>]+\?>', '', toko_data)
    product_data = re.sub(r'<\?xml[^>]+\?>', '', product_data)

    # Gabungkan keduanya dalam satu XML dengan root <data>
    xml_data = f'<?xml version="1.0" encoding="UTF-8"?>\n<data>\n<toko>{toko_data}</toko>\n<produk>{product_data}</produk>\n</data>'

    # Return hasil XML gabungan
    return HttpResponse(xml_data, content_type="application/xml")

def show_xml_toko_by_id(request, id):
    try:
        # Ambil data toko berdasarkan id
        toko = get_object_or_404(TokoEntry, pk=id)

        # Serialize data dari model TokoEntry berdasarkan id
        toko_data = serializers.serialize("xml", [toko])  # serialize toko sebagai list

        # Menghapus deklarasi XML <?xml ... ?> dari hasil serialisasi
        toko_data = re.sub(r'<\?xml[^>]+\?>', '', toko_data)

        # Return hasil XML dari toko saja
        xml_data = f'<?xml version="1.0" encoding="UTF-8"?>\n<toko>{toko_data}</toko>'
        return HttpResponse(xml_data, content_type="application/xml")

    except TokoEntry.DoesNotExist:
        return HttpResponse("<error>Toko with given ID does not exist.</error>", content_type="application/xml", status=404)

def show_xml_produk_by_id(request, id):
    try:
        # Ambil toko berdasarkan id
        product = get_object_or_404(ProductEntry, pk=id)

        # Serialize data dari model ProductEntry berdasarkan toko yang diambil
        product_data = serializers.serialize("xml", [product])

        # Menghapus deklarasi XML <?xml ... ?> dari hasil serialisasi
        product_data = re.sub(r'<\?xml[^>]+\?>', '', product_data)

        # Return hasil XML dari produk saja
        xml_data = f'<?xml version="1.0" encoding="UTF-8"?>\n<produk>{product_data}</produk>'
        return HttpResponse(xml_data, content_type="application/xml")

    except TokoEntry.DoesNotExist:
        return HttpResponse("<error>Toko with given ID does not exist.</error>", content_type="application/xml", status=404)

def show_json(request):
    # Serialize data dari model TokoEntry dan ProductEntry
    toko_data = serializers.serialize("json", TokoEntry.objects.all())
    product_data = serializers.serialize("json", ProductEntry.objects.all())

    # Mengubah string JSON menjadi list of dict agar bisa digabungkan
    toko_data = json.loads(toko_data)
    product_data = json.loads(product_data)

    # Gabungkan data menjadi satu dict dengan dua kunci: 'toko' dan 'produk'
    combined_data = {
        "toko": toko_data,
        "produk": product_data
    }

    # Return JSON response
    return JsonResponse(combined_data)

def all_toko_json(request):
    toko_list = TokoEntry.objects.all()
    data = [toko.to_json() for toko in toko_list]
    return JsonResponse({'toko': data})

def all_product_json(request):
    product_list = ProductEntry.objects.all()
    data = [product.to_json() for product in product_list]
    return JsonResponse({'products': data})

def show_json_toko_by_id(request, id):
    try:
        # Ambil data toko berdasarkan id
        toko = get_object_or_404(TokoEntry, pk=id)

        # Serialize data dari model TokoEntry berdasarkan id
        toko_data = serializers.serialize("json", [toko])  # serialize toko sebagai list

        # Mengubah string JSON menjadi list of dict agar lebih fleksibel
        toko_data = json.loads(toko_data)

        # Return hasil JSON dari toko saja
        return JsonResponse({"toko": toko_data}, safe=False)

    except TokoEntry.DoesNotExist:
        return JsonResponse({"error": "Toko with given ID does not exist."}, status=404)

def show_json_produk_by_id(request, id):
    try:
        # Ambil toko berdasarkan id
        product = get_object_or_404(ProductEntry, pk=id)

        # Serialize data dari model ProductEntry berdasarkan toko yang diambil
        product_data = serializers.serialize("json", [product])

        # Mengubah string JSON menjadi list of dict agar lebih fleksibel
        product_data = json.loads(product_data)

        # Return hasil JSON dari produk saja
        return JsonResponse({"produk": product_data}, safe=False)

    except TokoEntry.DoesNotExist:
        return JsonResponse({"error": "Toko with given ID does not exist."}, status=404)

def edit_toko(request, id):
    # Ambil data toko berdasarkan id
    toko = get_object_or_404(TokoEntry, pk=id)

    # Set TokoEntry sebagai instance dari form
    form = TokoEntryForm(request.POST or None, instance=toko)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman utama
        form.save()
        return HttpResponseRedirect(reverse('dashboard_admin:show_main'))

    context = {'form': form}
    return render(request, "edit_toko.html", context)

def edit_product(request, id):
    # Ambil data produk berdasarkan id
    product = get_object_or_404(ProductEntry, pk=id)

    # Set ProductEntry sebagai instance dari form
    form = ProductEntryForm(request.POST or None, request.FILES or None, instance=product)


    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman utama
        form.save()
        return HttpResponseRedirect(reverse('dashboard_admin:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_toko(request, id):
    toko = get_object_or_404(TokoEntry, pk=id)
    toko.delete()
    return HttpResponseRedirect(reverse('dashboard_admin:show_main'))

def delete_product(request, id):
    product = get_object_or_404(ProductEntry, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('dashboard_admin:show_main'))

class TokoEntryViewSet(viewsets.ModelViewSet):
    queryset = TokoEntry.objects.all()
    serializer_class = TokoEntrySerializer

class ProductEntryViewSet(viewsets.ModelViewSet):
    queryset = ProductEntry.objects.all()
    serializer_class = ProductEntrySerializer

    @action(detail=True, methods=['get'])
    def products_for_toko(self, request, pk=None):
        toko = self.get_object()
        products = toko.products.all()
        serializer = ProductEntrySerializer(products, many=True)
        return Response(serializer.data)
    
class ProductsForTokoView(APIView):
    def get(self, request, toko_id, format=None):
        products = ProductEntry.objects.filter(toko__id=toko_id)
        serializer = ProductEntrySerializer(products, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def products_for_toko_json(request, toko_id):
    try:
        # Mengambil semua produk berdasarkan toko_id
        products = ProductEntry.objects.filter(toko_id=toko_id)
        serializer = ProductEntrySerializer(products, many=True)
        return Response(serializer.data)
    except ProductEntry.DoesNotExist:
        return Response({'error': 'Products not found for this store'}, status=404)
    
@api_view(['POST'])
def create_product_flutter(request):
    if request.method == 'POST':
        data = request.data
        try:
            product = ProductEntry.objects.create(
                name=data['name'],
                price=data['price'],
                description=data['description'],
                image=data['image'],
                toko_id=data['toko'],
            )
            product.save()
            return Response({'status': 'success', 'message': 'Product added successfully!'}, status=201)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=400)
        
@api_view(['POST'])
def create_restaurant_flutter(request):
    if request.method == 'POST':
        data = request.data
        try:
            # Buat restoran baru
            restaurant = TokoEntry.objects.create(
                name=data['name'],
                location=data['location'],
            )
            restaurant.save()
            # Return data restoran yang baru dibuat
            return Response({
                'status': 'success',
                'message': 'Restaurant added successfully!',
                'restaurant': restaurant.to_json(),  # Kirim data restoran sebagai respons
            }, status=201)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=400)
        
@api_view(['GET'])
def get_products_by_toko(request, toko_id):
    try:
        print(f"Fetching products for toko_id: {toko_id}")
        # Fetch the products for the given toko_id (restaurant)
        products = ProductEntry.objects.filter(toko_id=toko_id)
        
        # Serialize the data
        serializer = ProductEntrySerializer(products, many=True)
        
        # Return the serialized data
        return Response(serializer.data, status=200)
    
    except ProductEntry.DoesNotExist:
        return Response({"message": "No products found for this restaurant."}, status=404)
    
@csrf_exempt
def delete_toko_flutter(request, id):
    if request.method == 'DELETE':
        try:
            # Ambil data restoran berdasarkan ID
            toko = get_object_or_404(TokoEntry, id=id)
            toko.delete()  # Hapus dari database
            return JsonResponse({'message': 'Restoran berhasil dihapus'}, status=200)
        except TokoEntry.DoesNotExist:
            return JsonResponse({'error': 'Restoran tidak ditemukan'}, status=404)
    else:
        return JsonResponse({'error': 'Metode tidak diizinkan'}, status=405)
    
@csrf_exempt
def update_toko_flutter(request, id):
    if request.method == 'PUT':
        try:
            toko = get_object_or_404(TokoEntry, id=id)
            data = json.loads(request.body)

            # Update fields
            toko.name = data.get('name', toko.name)
            toko.location = data.get('location', toko.location)
            toko.save()

            return JsonResponse({
                'message': 'Restoran berhasil diperbarui',
                'id': toko.id,
                'name': toko.name,
                'location': toko.location,
            }, status=200)
        except TokoEntry.DoesNotExist:
            return JsonResponse({'error': 'Restoran tidak ditemukan'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Metode tidak diizinkan'}, status=405)
    
@csrf_exempt
def delete_product_flutter(request, id):
    if request.method == 'DELETE':
        try:
            product = get_object_or_404(ProductEntry, id=id)
            product.delete()
            return JsonResponse({'message': 'Product deleted successfully'}, status=200)
        except ProductEntry.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def update_product_flutter(request, id):
    if request.method == 'PUT':
        try:
            product = get_object_or_404(ProductEntry, id=id)
            data = json.loads(request.body)

            # Update fields
            product.name = data.get('name', product.name)
            product.price = data.get('price', product.price)
            product.description = data.get('description', product.description)
            product.image = data.get('image', product.image)
            product.toko_id = data.get('toko_id', product.toko_id)
            product.save()

            return JsonResponse({'message': 'Product updated successfully'}, status=200)
        except ProductEntry.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['GET'])
def get_all_toko_names(request):
    try:
        toko_list = TokoEntry.objects.all()
        toko_data = [{"id": toko.id, "name": toko.name} for toko in toko_list]
        return JsonResponse({"toko_list": toko_data}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
