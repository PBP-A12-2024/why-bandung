from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
import uuid

# Create your models here.
class TokoEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    location = models.TextField()

    def __str__(self):
        return self.name
    
    def to_json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'location': self.location
        }

class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField()
    image = models.URLField(max_length=500, blank=True, null=True)
    toko = models.ForeignKey(TokoEntry, on_delete=models.CASCADE, related_name='products')

    def to_json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'image': self.image,
            'toko_id': str(self.toko.id),
            'toko_name': self.toko.name
        }