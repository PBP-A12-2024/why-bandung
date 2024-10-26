from django.shortcuts import render, redirect, get_object_or_404
from .forms import TokoEntryForm, ProductEntryForm
from .models import TokoEntry, ProductEntry
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.core.exceptions import ValidationError
import re
import json

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
        form = ProductEntryForm(request.POST, request.FILES)  # Tambahkan request.FILES untuk menangani file
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
    # Serialize data dari model TokoEntry dan ProductEntry
    toko_data = serializers.serialize("xml", TokoEntry.objects.all())
    product_data = serializers.serialize("xml", ProductEntry.objects.all())

    # Menghapus deklarasi XML <?xml ... ?> dari kedua hasil serialisasi
    toko_data = re.sub(r'<\?xml[^>]+\?>', '', toko_data)
    product_data = re.sub(r'<\?xml[^>]+\?>', '', product_data)

    # Gabungkan keduanya dalam satu XML dengan root <data>
    xml_data = f'<?xml version="1.0" encoding="UTF-8"?>\n<data>\n<toko>{toko_data}</toko>\n<produk>{product_data}</produk>\n</data>'

    # Return hasil XML gabungan
    return HttpResponse(xml_data, content_type="application/xml")

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

