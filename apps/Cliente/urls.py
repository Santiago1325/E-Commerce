from django.urls import path
from apps.Cliente.views import index

urlpatterns = [
 path('', index),
]
