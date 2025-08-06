"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_registros.registros, name="Principal"),
    path('contacto/', views_registros.contacto, name="Contacto"),
    path('formulario/', views.formulario, name="Formulario"),
    path('ejemplo/', views.ejemplo, name="Ejemplo"),
    path('registrar/', views_registros.registrar, name="Registrar"),
    path('comentarios/', views_registros.mostrar_comentarios, name="Comentarios"),
    path('eliminarComentario/<int:id>/', views_registros.eliminarComentarioContacto, name='Eliminar'),
    path('subir',views_registros.archivos,name="Subir"),

    path('consultas/', views_registros.consultas, name='consultas'),
    path('consultas2/', views_registros.consultar2, name='consultas2'),
    path('consultas3/', views_registros.consultar3, name='consultas3'),
    path('consultas4/', views_registros.consultar4, name='consultas4'),
    path('consultas5/', views_registros.consulta5, name='consultas5'),
    path('consultas6/', views_registros.consulta6, name='consultas6'),
    path('consultas7/', views_registros.consultar7, name='consultas7'),
    path('consultas8/', views_registros.consultar8, name='consultas8'),
    path('consultas9/', views_registros.consultar9, name='consultas9'),
    path('consultas10/', views_registros.consultar10, name='consultas10'),
    path('consultas11/', views_registros.consultar11, name='consultas11'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)