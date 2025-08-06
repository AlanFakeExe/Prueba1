from django.urls import path
from . import views

urlpatterns = [
    path('consultar_comentarios/', views.consultar_comentarios, name='consultar_comentarios'),
    path('editar_comentario/<int:id>/', views.editar_comentario, name='editar_comentario'),
    path('eliminar_comentario/<int:id>/', views.eliminar_comentario, name='eliminar_comentario'),
    
]
