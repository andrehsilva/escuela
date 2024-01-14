from django.db import models
from tenant.models import Tenant

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=255)
    namesocial = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True)
    namefantasy = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=True)


    # Relacionamento com Tenant
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='schools')
   

    class Meta:
        verbose_name = ("Escola")
        verbose_name_plural = ("Escolas")
        ordering = ['-name', '-created_at']

    def __str__(self):
        return self.name