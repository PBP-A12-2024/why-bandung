# serializers.py
from rest_framework import serializers
from .models import TokoEntry, ProductEntry

class TokoEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TokoEntry
        fields = ['id', 'name', 'location']

class ProductEntrySerializer(serializers.ModelSerializer):
    toko_name = serializers.CharField(source='toko.name', read_only=True)

    class Meta:
        model = ProductEntry
        fields = ['id', 'name', 'price', 'description', 'image', 'toko_id', 'toko_name']
