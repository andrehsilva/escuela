from django.urls import path
from .views import SchoolView

urlpatterns = [
    path('school/index/', SchoolView.as_view(), name="school"),
]