from django.contrib import admin
from Apps.ejemplares.models import Ejemplares, Prestar
# Register your models here.

class EjemplaresAdmin(admin.ModelAdmin):
    pass

admin.site.register(Prestar)
admin.site.register(Ejemplares, EjemplaresAdmin)