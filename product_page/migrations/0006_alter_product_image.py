# Generated by Django 5.1.1 on 2024-10-25 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_page', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='img/'),
        ),
    ]