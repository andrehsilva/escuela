# Generated by Django 5.0.1 on 2024-01-20 11:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0002_tenant_hash_value_tenant'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='activated',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]