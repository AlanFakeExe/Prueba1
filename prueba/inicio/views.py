from django.shortcuts import render, HttpResponse
from registros.models import Comentarios


menu = """
<a href="/">Home</a>
<a href="/formulario">Registrar</a>
<a href="/contacto">Contáctanos</a>
r
"""

def principal(request):
    return render(request, "inicio/principal.html")

def contacto(request):
   return render(request,"inicio/contacto.html")

def formulario(request):
       return render(request,"inicio/formulario.html")

def ejemplo(request):
   return render(request,"inicio/ejemplo.html")

def consultar_comentarios(request):
    comentarios = Comentarios.objects.all()
    return render(request, "inicio/consultar_comentarios.html", {
        'comentarios': comentarios
    })