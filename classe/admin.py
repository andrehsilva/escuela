from django.contrib import admin
from .models import Classe, Period, Serie, Segment

# Register your models here.
admin.site.register(Classe)
admin.site.register(Period)
admin.site.register(Segment)
admin.site.register(Serie)