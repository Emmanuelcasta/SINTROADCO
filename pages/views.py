from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "pages/inicio.html"

class GaleriaPageView(TemplateView):  # Cambiar a CamelCase
    template_name = "pages/galeria.html"

class InformacionPageView(TemplateView):  # Cambiar a CamelCase
    template_name = "pages/informacion.html"

class ContactoPageView(TemplateView):  # Cambiar a CamelCase
    template_name = "pages/contacto.html"
