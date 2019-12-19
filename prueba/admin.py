from django.contrib import admin
from .models import Prueba
from .models import test

# Register your models here.
class PruebasAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_examen',)

class TestAdmin(admin.ModelAdmin):
    readonly_fields = ('resultado',)

admin.site.register(Prueba,PruebasAdmin)
admin.site.register(test,TestAdmin)