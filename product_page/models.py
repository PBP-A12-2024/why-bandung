from django.db import models
from django.contrib.auth.models import User
from dashboard_admin.models import ProductEntry
import uuid

class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(max_length=500, blank=True, null=True)
    hashtags = models.ManyToManyField('Hashtag', blank=True)  
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

class Hashtag(models.Model):
    tag = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'#{self.tag}'

class Review(models.Model):
    product = models.ForeignKey(ProductEntry, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name} ({self.rating}/5)'

