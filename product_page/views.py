from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from dashboard_admin.models import ProductEntry, TokoEntry
from .forms import ReviewForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import csv
import csv
from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages

def product_page(request):
    # Ambil parameter filter dari request
    name_filter = request.GET.get('name', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    toko_filter = request.GET.get('toko')
    category = request.GET.get('category')  # Ambil kategori dari request
    location = request.GET.get('location')  # Ini untuk filter lokasi

    # Mulai query dasar untuk semua produk
    products = ProductEntry.objects.all()

    # Filter berdasarkan nama jika diisi
    if name_filter:
        products = products.filter(name__icontains=name_filter)

    # Filter berdasarkan harga minimal dan maksimal
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Filter berdasarkan toko jika diisi
    if toko_filter:
        products = products.filter(toko__id=toko_filter)
    if category:
        products = products.filter(description__iexact=category)
    if location:
        products = products.filter(toko__location__icontains=location)
    all_categories = ProductEntry.objects.values_list('description', flat=True).distinct()
    all_locations = TokoEntry.objects.values_list('location', flat=True).distinct()

    # Dapatkan daftar semua toko untuk dropdown filter
    all_toko = TokoEntry.objects.all()

    return render(request, 'product_page.html', {
        'products': products,
        'all_toko': all_toko,
        'all_categories': all_categories,  # Data kategori
        'all_locations': all_locations,  # Data lokasi

    })

@login_required
@csrf_exempt
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Pastikan ini mengacu pada model yang benar
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return JsonResponse({'message': 'Review submitted successfully'}, status=200)
        else:
            return JsonResponse({'message': 'Form data is invalid'}, status=400)
    return JsonResponse({'message': 'Invalid request method'}, status=405)



def import_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        
        # Periksa apakah file yang diunggah adalah CSV
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File yang diunggah bukan CSV')
            return redirect('import_csv')
        
        # Membaca file CSV
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            # Menemukan atau membuat TokoEntry berdasarkan nama toko di CSV
            toko, created = TokoEntry.objects.get_or_create(
                name=row['TOKO'],
                defaults={'location': row['LOKASI']}
            )
            
            # Menyimpan atau memperbarui data ProductEntry menggunakan toko yang ditemukan/dibuat
            ProductEntry.objects.update_or_create(
                name=row['NAMA_PRODUK'],
                defaults={
                    'price': row['HARGA_RETAIL'],
                    'description': row['KATEGORI'],
                    'toko': toko
                }
            )
        
        messages.success(request, 'Data CSV berhasil diimpor ke database.')
        return redirect('import_csv')
    
    return render(request, 'import_csv.html')
