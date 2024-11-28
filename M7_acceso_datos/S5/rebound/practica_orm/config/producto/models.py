from django.db import models

# Create your models here.
class Fabrica(models.Model):
    nombre = models.CharField(max_length=255)

class Producto(models.Model):
    nombre = models.TextField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=100)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, blank=True, null=True)
    # fabrica = models.OneToOneField(Fabrica, on_delete=models.CASCADE, blank=True, null= True)
    # fabrica = models.ManyToManyField(Fabrica)