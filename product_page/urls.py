from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('product_page/', views.product_page, name='product_page'),
    path('import-csv/', views.import_csv, name='import_csv'),
    path('product_page/<uuid:product_id>/', views.product_detail, name='product_detail'),
    path('product_page/<uuid:product_id>/add-review/', views.add_review, name='add_review'),
    path('product_page/<uuid:product_id>/edit-review/<int:review_id>/', views.edit_review, name='edit_review'),  # Edit review
    path('product_page/<uuid:product_id>/delete-review/<int:review_id>/', views.delete_review, name='delete_review'),  # Delete review
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
