
# Generated by Django 5.1.2 on 2024-10-26 13:22

import dashboard_admin.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_admin', '0006_alter_productentry_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productentry',
            name='image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
