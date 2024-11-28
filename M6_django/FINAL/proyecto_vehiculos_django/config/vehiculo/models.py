from django.db import models
import datetime

# Create your models here.
# Marca: Fiat, Chevrolet, Ford y Toyota.
# 20 caracteres como máximo, y por defecto Ford.
# Modelo: 100 caracteres como máximo.
# Serial Carrocería: 50 caracteres como máximo.
# Serial Motor: 50 caracteres como máximo.
# Categoría: Particular, transporte y carga. 20 caracteres como máximo, y por defecto Particular.
# Precio.
# Fecha de creación.
# Fecha de modificación.

class Vehiculo(models.Model):
    MARCA = {('FIAT','Fiat'), ('CHEVROLET', 'Chevrolet'), ('FORD', 'Ford'), ('TOYOTA', 'Toyota')}
    CATEGORIA = {('PARTICULAR', 'Particular'), ('TRANSPORTE', 'Transporte'), ('CARGA', 'Carga')}
    marca = models.CharField(max_length=20, default='FORD', choices=MARCA)
    modelo = models.TextField(max_length=100)
    serial_carroceria = models.TextField(max_length=50)
    serial_motor = models.TextField(max_length=50)
    categoria = models.CharField(max_length=20, default='PARTICULAR', choices=CATEGORIA)
    precio = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now())
    fecha_modificacion = models.DateTimeField(default=datetime.datetime.now())
