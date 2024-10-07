from django.urls import path
from .views import HomePageView, GaleriaPageView, InformacionPageView, ContactoPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='inicio'),
    path('galeria/', GaleriaPageView.as_view(), name='galeria'),  # Cambiado a GaleriaPageView
    path('informacion/', InformacionPageView.as_view(), name='informacion'),  # Cambiado a InformacionPageView
    path('contacto/', ContactoPageView.as_view(), name='contacto'),  # Cambiado a ContactoPageView
]
