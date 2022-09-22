from django.urls import path
from Apps.usuarios.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]
