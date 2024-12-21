from django.urls import path
from .views import show_main, create_toko_entry, create_product_entry, show_xml, show_json, edit_toko, edit_product, delete_toko, delete_product, show_xml_toko_by_id, show_xml_produk_by_id, show_json_toko_by_id, show_json_produk_by_id
from .views import all_toko_json, all_product_json, products_for_toko_json, create_product_flutter, create_restaurant_flutter, get_products_by_toko
from .views import delete_toko_flutter, update_toko_flutter, delete_product_flutter, update_product_flutter, get_all_toko_names
from django.conf import settings
from django.conf.urls.static import static

app_name = 'dashboard_admin'

urlpatterns = [
    # Halaman utama dan manajemen toko/produk
    path('', show_main, name='show_main'),
    path('create-toko/', create_toko_entry, name='create_toko_entry'),
    path('create-product/', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name="show_json"),
    path('xml/toko/<str:id>/', show_xml_toko_by_id, name="show_xml_toko_by_id"),
    path('xml/produk/<str:id>/', show_xml_produk_by_id, name="show_xml_produk_by_id"),
    path('json/toko/<str:id>/', show_json_toko_by_id, name="show_json_toko_by_id"),
    path('json/produk/<str:id>/', show_json_produk_by_id, name="show_json_produk_by_id"),
    path('edit-toko/<uuid:id>', edit_toko, name="edit_toko"),
    path('edit-product/<uuid:id>', edit_product, name="edit_product"),
    path('delete-toko/<uuid:id>/', delete_toko, name="delete_toko"),
    path('delete-product/<uuid:id>', delete_product, name="delete_product"),
    
    # Route untuk mendapatkan semua data toko dan produk dalam format JSON
    path('all-toko/', all_toko_json, name='all_toko_json'),
    path('all-product/', all_product_json, name='all_product_json'),

    # Menambahkan route untuk mengambil produk berdasarkan toko yang dipilih
    # Menggunakan produk_for_toko_json yang sudah didefinisikan di views.py
    path('json/products-for-toko/<uuid:toko_id>/', products_for_toko_json, name='products_for_toko_json'),
    path('create-product-flutter/', create_product_flutter, name='create_product_flutter'),
    path('create-restaurant-flutter/', create_restaurant_flutter, name='create_restaurant_flutter'),
    path('get-products-by-toko/<uuid:toko_id>/', get_products_by_toko, name='get_products_by_toko'),
    path('delete-toko-flutter/<uuid:id>/', delete_toko_flutter, name='delete_toko_flutter'),
    path('update-toko-flutter/<uuid:id>/', update_toko_flutter, name='update_toko_flutter'),
    path('delete-product-flutter/<uuid:id>/', delete_product_flutter, name='delete_product_flutter'),
    path('update-product-flutter/<uuid:id>/', update_product_flutter, name='update_product_flutter'),
    path('get-all-toko-names/', get_all_toko_names, name='get_all_toko_names')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
