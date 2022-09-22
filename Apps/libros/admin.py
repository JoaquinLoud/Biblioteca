from django.contrib import admin
from Apps.libros.models import Libro, Escribir, Autor
# Register your models here.

class LibroAdmin(admin.ModelAdmin):
    list_display= ("titulo","numero_pagina","editorial","isbn")
    ordering= ("titulo",)
admin.site.register(Autor)
admin.site.register(Escribir)
admin.site.register(Libro, LibroAdmin)