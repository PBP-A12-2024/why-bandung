# Generated by Django 5.1.2 on 2024-10-23 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_admin', '0004_productentry_p_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productentry',
            old_name='p_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='productentry',
            old_name='p_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='productentry',
            old_name='p_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='productentry',
            old_name='p_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='productentry',
            old_name='p_toko',
            new_name='toko',
        ),
    ]
