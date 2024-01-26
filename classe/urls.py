from django.urls import path
from .views import ClasseView

urlpatterns = [
    path('classe/index/', ClasseView.as_view(), name="classe"),
]