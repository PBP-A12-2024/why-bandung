# Generated by Django 5.1.2 on 2024-10-27 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_page', '0007_alter_review_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]