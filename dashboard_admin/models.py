from django.db import models
from django.core.validators import MinValueValidator
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
    name = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    toko = models.ForeignKey(TokoEntry, on_delete=models.CASCADE, related_name='products')