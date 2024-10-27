import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from dashboard_admin.models import ProductEntry, TokoEntry
from .forms import ReviewForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import csv
import os
from django.shortcuts import render, redirect
from .models import Product, Review
from django.contrib import messages
from dashboard.models import JournalEntry

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render, redirect  
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.utils.html import strip_tags

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

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
    
def product_detail(request, product_id):
    product = get_object_or_404(ProductEntry, id=product_id)  # sesuaikan dengan tipe data
    return render(request, 'product_detail.html', {'product': product})


@login_required
@csrf_exempt  # Hanya untuk pengujian, pastikan untuk menghapus ini dalam produksi
def add_review(request, product_id):
    if request.method == 'POST':
        try:
            # Ambil data dari request
            user = request.user
            rating = request.POST.get('rating')
            comment = request.POST.get('comment')

            # Validasi data
            if not rating or not comment:
                return JsonResponse({'success': False, 'message': 'Rating and comment are required'}, status=400)
            
            # Pastikan rating dalam rentang 1-5
            rating = int(rating)
            if rating < 1 or rating > 5:
                return JsonResponse({'success': False, 'message': 'Rating must be between 1 and 5'}, status=400)

            # Pastikan ProductEntry ditemukan
            product = ProductEntry.objects.get(id=product_id)

            # Buat atau update ulasan
            review, created = Review.objects.update_or_create(
                user=user,
                product=product,
                defaults={
                    'rating': rating,
                    'comment': comment
                }
            )
            
            # Respons JSON
            return JsonResponse({
                'success': True,
                'username': user.username,
                'rating': review.rating,
                'comment': review.comment,
                'created_at': review.created_at.strftime('%B %d, %Y, %I:%M %p')
            })
        
        except ProductEntry.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Product not found'}, status=404)
        
        except ValueError:
            return JsonResponse({'success': False, 'message': 'Invalid rating value'}, status=400)
        
        except Exception as e:
            print("Error:", e)  # Debug
            return JsonResponse({'success': False, 'message': 'An error occurred'}, status=500)
    
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)


def import_csv(request):
    # Define the path to the CSV file
    csv_file_path = "static/csv/data.csv"  # Adjust this to the correct path of your CSV file
    
    # Check if the file exists
    if not os.path.exists(csv_file_path):
        messages.error(request, 'CSV file not found.')
        return render(request, 'import_csv.html')

    # Read and process the CSV file
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Process and store the data in the database
                toko, created = TokoEntry.objects.get_or_create(
                    name=row['TOKO'],
                    defaults={'location': row['LOKASI']}
                )
                
                ProductEntry.objects.update_or_create(
                    name=row['NAMA_PRODUK'],
                    defaults={
                        'price': row['HARGA_RETAIL'],
                        'description': row['KATEGORI'],
                        'image': row['URL'],
                        'toko': toko
                    }
                )
                
        messages.success(request, 'Data CSV successfully imported into the database.')
    except Exception as e:
        messages.error(request, f'Error processing the CSV file: {e}')

    return render(request, 'import_csv.html')

@login_required
@csrf_exempt
def edit_review(request, product_id, review_id):
    try:
        review = Review.objects.get(id=review_id, product_id=product_id, user=request.user)

        # Load data JSON dari body permintaan
        data = json.loads(request.body)

        # Update rating dan comment
        review.rating = data['rating']
        review.comment = data['comment']
        review.save()

        return JsonResponse({
            "success": True,
            "username": review.user.username,
            "rating": review.rating,
            "comment": review.comment
        })
    except Review.DoesNotExist:
        return JsonResponse({"success": False, "message": "Review not found."})
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)})

    
@login_required
@csrf_exempt
def delete_review(request, product_id, review_id):
    if request.method == 'DELETE':
        try:
            review = Review.objects.get(id=review_id, product_id=product_id)
            review.delete()
            return JsonResponse({'success': True, 'message': 'Review deleted successfully'})
        except Review.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Review not found'}, status=404)
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

def list_reviews(request):
    reviews = Review.objects.all().values("id", "food_name", "rating", "review_text", "created_at")
    return JsonResponse(list(reviews), safe=False, status=200)