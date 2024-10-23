from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/5.1/topics/db/models/
# https://www.w3schools.com/django/django_models.php
class Book(models.Model):
    # atributos
    titulo = models.CharField(max_length = 100, null = False)
    autor = models.CharField(max_length = 50, null = False)
    valoracion = models.IntegerField(help_text = 'Valoración entre 0 y 100')