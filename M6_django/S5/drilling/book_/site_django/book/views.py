from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class IndexPageView(TemplateView): # un view o controlador con una clase
    template_name = 'index.html'