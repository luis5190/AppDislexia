from django.db import models
from . choices import GENERO

class Prueba(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_nacimiento=models.DateField(null=True)
    habla_castellano=models.BooleanField(null=True)
    genero=models.CharField(choices=GENERO, max_length=100, null=True)
    fecha_examen=models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Prueba"
        verbose_name_plural= "Pruebas"
        ordering = ["-fecha_examen"]
        
    def __str__(self):
        return self.nombre

class test(models.Model):
    p1_p1=models.CharField(max_length=10)
    resultado = models.CharField(max_length=20, null=True)

    class Meta:
        verbose_name="Test"
        verbose_name_plural="Tests"

        def __str__(self):
            return self.p1_p1