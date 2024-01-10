from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome do grupo escolar.")
    email = models.EmailField(unique=True, verbose_name="E-mail de contato oficial do grupo escolar.")

    def __str__(self):
        return str(self.name)