from django.db import models
from school.models import School
import hashlib
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Period(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Segment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Serie(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=True)
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE, related_name='segment')

    def __str__(self):
        return self.name

class Classe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=True)
    # Relacionamento com Tenant
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='schools')
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='serie', default=1)
    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='period')


    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        ordering = ['-name', '-created_at']


    def __str__(self):
        return self.name