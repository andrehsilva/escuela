from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include ## adicionar include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tenant.urls')),
    path('', include('school.urls')),
    path('', include('classe.urls')),
]