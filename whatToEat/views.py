from django.shortcuts import render
from django.http import JsonResponse
from dashboard_admin.models import ProductEntry
from product_page.views import product_detail

# Create your views here.
def show_slider(request):
    return render(request, 'whatToEat.html')


def get_products(request):
    products = ProductEntry.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'image': product.image,
            'toko_name': product.toko.name
        }
        for product in products
    ]
    return JsonResponse(data, safe=False)

def get_detail(request, product_id):
    product_detail(request, product_id)