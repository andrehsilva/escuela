from django.db import models
from tenant.models import Tenant
import hashlib
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=255)
    namesocial = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True)
    namefantasy = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=True)
    hash_value = models.CharField(max_length=16, blank=True, null=True, unique=True)
    # Relacionamento com Tenant
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='schools')

@receiver(pre_save, sender=School)
def generate_hash(sender, instance, **kwargs):
    if not instance.hash_value:
        # Gera um hash usando o cnpj como base
        hash_input = instance.cnpj.encode('utf-8')
        hash_result = hashlib.md5(hash_input).hexdigest()[:16]
        instance.hash_value = hash_result
   

    class Meta:
        verbose_name = ("Escola")
        verbose_name_plural = ("Escolas")
        ordering = ['-name', '-created_at']

    def __str__(self):
        return self.name