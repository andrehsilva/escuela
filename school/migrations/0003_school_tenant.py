# Generated by Django 5.0.1 on 2024-01-24 22:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_school_options_remove_school_tenant_and_more'),
        ('tenant', '0003_tenant_activated_tenant_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='tenant',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='tenant.tenant'),
        ),
    ]
