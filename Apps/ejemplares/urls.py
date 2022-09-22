from django.urls import path
from Apps.ejemplares.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]