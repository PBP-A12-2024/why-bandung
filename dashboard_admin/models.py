from django.db import models
from django.core.validators import MinValueValidator
import uuid
import os

def get_image_filename(instance, filename):
    # Ekstrak ekstensi file yang diupload (misalnya .jpg, .png)
    ext = filename.split('.')[-1]
    
    # Format nama file baru berdasarkan id produk
    filename = f"{instance.id}.{ext}"
    
    # Tentukan folder penyimpanan gambar
    return os.path.join('product_images/', filename)

# Create your models here.
class TokoEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    location = models.TextField()

    def __str__(self):
        return self.name

class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField()
    image = models.ImageField(upload_to=get_image_filename, blank=True, null=True)
    toko = models.ForeignKey(TokoEntry, on_delete=models.CASCADE, related_name='products')