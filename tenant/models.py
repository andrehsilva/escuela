from django.db import models
import hashlib
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Tenant(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome do grupo escolar.")
    email = models.EmailField(unique=True, verbose_name="E-mail de contato oficial do grupo escolar.")
    created_at = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=True)
    hash_value_tenant = models.CharField(max_length=16, blank=True, null=True, unique=True)

@receiver(pre_save, sender=Tenant)
def generate_tenant_hash(sender, instance, **kwargs):
    if not instance.hash_value_tenant:
        # Gera um hash usando o email como base
        hash_input = instance.email.encode('utf-8')
        hash_result = hashlib.md5(hash_input).hexdigest()[:16]
        instance.hash_value_tenant = hash_result

def __str__(self):
    return str(self.name)