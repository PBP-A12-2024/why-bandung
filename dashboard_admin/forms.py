from django.forms import ModelForm
from dashboard_admin.models import TokoEntry, ProductEntry
from django import forms

class TokoEntryForm(ModelForm):
    class Meta:
        model = TokoEntry
        fields = ['name', "location"]

    def clean_nama_toko(self):
        name = self.cleaned_data.get('name')
        if TokoEntry.objects.filter(name=name).exists():
            raise forms.ValidationError("Nama toko sudah digunakan, silahkan gunakan nama lain")
        return name

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry

        fields = ["name", "price", "description", "image", "toko"]

    def clean(self):
        cleaned_data = super().clean()
        toko = TokoEntry.objects.all()
        
        # Cek apakah ada toko yang sudah terdaftar
        if not toko.exists():
            raise forms.ValidationError("Tidak ada toko yang tersedia. Anda harus menambahkan toko sebelum menambahkan produk.")
        
        return cleaned_data

