from django.shortcuts import render
from django.http import JsonResponse
from dashboard_admin.models import TokoEntry, ProductEntry

# Create your views here.
def show_map(request):
    return render(request, "geomap.html")

def filter_tokos(request):
    lokasi = request.GET.get('lokasi', None)
    if lokasi:
        # Filter TokoEntry based on location
        tokos = TokoEntry.objects.filter(location=lokasi).values('id', 'name', 'location')  # Adjust based on your model fields
        return JsonResponse(list(tokos), safe=False)
    return JsonResponse([], safe=False)

def filter_products_by_toko(request):
    toko_id = request.GET.get('toko_id', None)
    if toko_id:
        # Retrieve products for the specified TokoEntry
        products = ProductEntry.objects.filter(p_toko__name=toko_id).values('id', 'name', 'price', 'description')  # Adjust based on your model fields
        return JsonResponse(list(products), safe=False)
    return JsonResponse([], safe=False)