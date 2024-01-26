# Generated by Django 5.0.1 on 2024-01-26 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classe', '0002_alter_classe_options_remove_classe_hash_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='classe',
            name='segment',
            field=models.CharField(choices=[('off', ''), ('ei', 'Educação Infantil'), ('ef1', 'Educação anos Iniciais'), ('ef2', 'Educação Anos Finais'), ('em', 'Ensino Médio'), ('pre', 'Pré Vestibular')], default='regular', max_length=10),
        ),
    ]