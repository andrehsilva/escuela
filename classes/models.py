from django.db import models
from school.models import School
import hashlib
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Classes(models.Model):
    PERIOD_CHOICES = [
        ('morning', 'Manhã'),
        ('afternoon', 'Tarde'),
        ('evening', 'Noite'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES, default='morning')
    created_at = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=True)
    hash_value = models.CharField(max_length=16, blank=True, null=True, unique=True)
    # Relacionamento com Tenant
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='schools')

@receiver(pre_save, sender=Classes)
def generate_hash(sender, instance, **kwargs):
    if not instance.hash_value:
        # Gera um hash usando o cnpj como base
        hash_result = hashlib.md5().hexdigest()[:16]
        instance.hash_value = hash_result

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        ordering = ['-name', '-created_at']

    def __str__(self):
        return self.name