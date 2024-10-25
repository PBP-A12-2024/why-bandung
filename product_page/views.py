from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Review, Hashtag
from .forms import ReviewForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def product_page(request):
    product = Product.objects.first()  # Mengambil produk pertama, atau sesuaikan dengan kebutuhan
    if product:
        reviews = product.reviews.all()  # Mengambil review terkait produk
        hashtags = product.hashtags.all()
        return render(request, 'product_page.html', {
            'product': product,
            'reviews': reviews,
            'hashtags': hashtags
        })
    else:
        # Jika tidak ada produk
        return render(request, 'product_page.html', {
            'message': 'Tidak ada produk yang tersedia.'
        })


@login_required
@csrf_exempt  
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
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
