from django.contrib import admin
from .models import Prueba

# Register your models here.
class PruebasAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_examen',)

admin.site.register(Prueba,PruebasAdmin)