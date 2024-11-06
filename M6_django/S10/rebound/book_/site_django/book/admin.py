from django.contrib import admin
from .models import Book

# Register your models here.
# https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin
admin.site.register(Book) # registro de los model separados por coma
