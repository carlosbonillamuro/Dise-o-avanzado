from django.urls import path
from .views import funcion_hola, funcion_calculadora


urlpatterns = [
    path('hola/', funcion_hola),
    path('calculadora/', funcion_calculadora),
]
