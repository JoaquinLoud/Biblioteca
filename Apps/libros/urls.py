from django.urls import path
from Apps.libros.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]
