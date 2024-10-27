from django.urls import path
from whatToEat.views import show_slider, get_products, get_detail

app_name = 'card'

urlpatterns = [
    path('', show_slider, name='WhatToEat'),
    path('get_products/', get_products, name='get_products'),
    path('product_page/<uuid:product_id>/', get_detail, name='get_detail'),
]