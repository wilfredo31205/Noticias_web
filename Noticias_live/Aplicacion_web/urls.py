from django.urls import path,include
from .views import Inicio, detalleView,detallesegmentos,detalles_noticias,deportes,musica,politica,OpinionView,detalleViewopinion,Buscarview,contacto
#from .views import *
#from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

app_name= 'news_app'
urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('Inicio/',Inicio.as_view(),name = 'index'),
    path('detalles/<int:pk>/<slug:slug>',detalleView.as_view(), name='detail'),
    path('detalles1/<int:pk>', detallesegmentos.as_view(), name='detail_segmento'),
    path('detalles_noticias/<int:pk>/', detalles_noticias.as_view(), name='detail_noticias'),
    path('detalles_opinion/<int:pk>/', detalleViewopinion.as_view(), name='detailopinion'),
    path('deportes/',deportes.as_view(), name='deportes'),
    path('Musica/',musica.as_view(), name='Musica'),
    path('buscar/',Buscarview.as_view(), name='buscar'),
    path('politica/',politica.as_view(), name='politica'),
    path('opiniones/',OpinionView.as_view(), name='opinion'),
    path('contacto/',contacto,name="contacto"),

    #cuando cambies solo deber ser localhost/deportes/ pra listar post sobre deportes, si, se me habia olvidado quitar el pk id



] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )


