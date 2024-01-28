# Generated by Django 5.0.1 on 2024-01-26 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classe', '0003_classe_segment'),
    ]

    operations = [
        migrations.AddField(
            model_name='classe',
            name='series',
            field=models.CharField(blank=True, choices=[], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='classe',
            name='segment',
            field=models.CharField(choices=[('off', ''), ('ei', 'Educação Infantil'), ('ef1', 'Educação anos Iniciais'), ('ef2', 'Educação Anos Finais'), ('em', 'Ensino Médio'), ('pre', 'Pré Vestibular')], default='off', max_length=10),
        ),
    ]
