# Generated by Django 5.0.1 on 2024-01-10 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome do grupo escolar.')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail de contato oficial do grupo escolar.')),
            ],
        ),
    ]
