from django.urls import path
from .views import calculate_rule

urlpatterns = [
    path('apply/', calculate_rule)
]