from django.db import models
import uuid

# Create your models here.
class TokoEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    location = models.TextField()

    def __str__(self):
        return self.name

class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    p_name = models.CharField(max_length=255)
    p_price = models.IntegerField()
    p_description = models.TextField()
    p_image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    p_toko = models.ForeignKey(TokoEntry, on_delete=models.CASCADE, related_name='products')