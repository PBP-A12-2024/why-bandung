from django.urls import path
from whatToEat.views import show_slider

app_name = 'main'

urlpatterns = [
    path('', show_slider, name='WhatToEat'),
]