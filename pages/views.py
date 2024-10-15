from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = "templates/pages/inicio.html"

class GaleriaPageView(TemplateView):  # Cambiar a CamelCase
    template_name = "templates/pages/galeria.html"

class InformacionPageView(TemplateView):  # Cambiar a CamelCase
    template_name = "templates/pages/informacion.html"

class ContactoPageView(TemplateView):
    template_name = "templates/pages/contacto.html"

    def post(self, request, *args, **kwargs):
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        # Asunto y cuerpo del correo
        subject = f'Mensaje de {nombre} desde el formulario de contacto'
        message = f'Nombre: {nombre}\nEmail: {email}\n\nMensaje:\n{mensaje}'

        # Remitente y destinatarios
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['SINTROADCOpresidencia@hotmail.com']  # Correo destino

        # Envía el correo
        send_mail(subject, message, from_email, recipient_list)

        # Define y muestra el mensaje de éxito
        messages.success(request, 'Tu mensaje ha sido enviado con éxito. Nos pondremos en contacto contigo pronto.')

        # Renderiza la misma página con el mensaje de éxito
        return render(request, self.template_name)