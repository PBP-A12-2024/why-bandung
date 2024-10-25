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
    # Mengambil semua produk dan menampilkan toko terkait
    products = ProductEntry.objects.all()
    if products:
        return render(request, 'product_page.html', {
            'products': products
        })
    else:
        # Jika tidak ada produk
        return render(request, 'product_page.html', {
            'message': 'Tidak ada produk yang tersedia.'
        })

@login_required
@csrf_exempt
def add_review(request, product_id):
    # Mengambil produk berdasarkan id menggunakan model ProductEntry
    product = get_object_or_404(ProductEntry, id=product_id)
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
