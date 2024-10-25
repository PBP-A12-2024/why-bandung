from django.urls import path
from .views import show_main, create_toko_entry, create_product_entry, show_xml, show_json, edit_toko, edit_product, delete_toko, delete_product

app_name = 'dashboard_admin'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-toko/', create_toko_entry, name='create_toko_entry'),
    path('create-product/', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name="show_json"),
    path('edit-toko/<uuid:id>', edit_toko, name="edit_toko"),
    path('edit-product/<uuid:id>', edit_product, name="edit_product"),
    path('delete-toko/<uuid:id>/', delete_toko, name="delete_toko"),
    path('delete-product/<uuid:id>', delete_product, name="delete_product")
]