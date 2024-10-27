from django.urls import path
from .views import show_map,filter_tokos,filter_products_by_toko

app_name = 'geomapping'

urlpatterns = [
    path('map-show/', show_map, name='show_map'),
    path('map-show/filter-tokos/', filter_tokos, name='filter_tokos'),
    path('map-show/filter-products-by-toko/', filter_products_by_toko, name='filter_products_by_toko'),
]