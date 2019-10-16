from django.db import models

# Create your models here.
class Project(models.Model):
    titulo=models.CharField(max_length=200)
    detalle=models.TextField(null=True)
    imagen=models.ImageField(null=True,upload_to="projects")
    fecha_creacion=models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-fecha_creacion"]
    def __str__(self):
        return self.titulo
