from django.db import models
from school.models import School
import hashlib
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Classe(models.Model):
    PERIOD_CHOICES = [
        ('morning', 'Manhã'),
        ('afternoon', 'Tarde'),
        ('evening', 'Noite'),
    ]

    SEGMENT_CHOICES = [
        ('off', ''),
        ('ei', 'Educação Infantil'),
        ('ef1', 'Educação anos Iniciais'),
        ('ef2', 'Educação Anos Finais'),
        ('em', 'Ensino Médio'),
        ('pre', 'Pré Vestibular'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES, default='morning')
    segment = models.CharField(max_length=10, choices=SEGMENT_CHOICES, default='off')
    created_at = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=True)
    # Relacionamento com Tenant
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='schools')

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        ordering = ['-name', '-created_at']

    def __str__(self):
        return self.name
