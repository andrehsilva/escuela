from django.urls import path
from .views import TenantView

urlpatterns = [
    path('tenant/index/', TenantView.as_view(), name="tenant"),
]