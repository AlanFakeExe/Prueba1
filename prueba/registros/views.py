from django.shortcuts import render, redirect
from .models import Alumnos
from .models import ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages
import datetime


def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {"alumnos": alumnos})

def mostrar_comentarios(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

def registrar(request): 
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Comentarios')  
    else:
        form = ComentarioContactoForm()
    return render(request, 'registros/contacto.html', {'form': form})

def contacto(request):
    return render(request, "registros/contacto.html")

def eliminarComentarioContacto(request, id,confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentarios.html",{'comentarios':comentarios})

    return render(request, confirmacion, {'object':comentario})

def consultas(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar2(request):
    alumnos = Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar3(request):
    alumnos = Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request, "registros/consultas.html", {"alumnos": alumnos})


def consulta5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Elena", "Rey"])
    return render(request, "registros/consultas.html", {"alumnos":alumnos})


def consulta6(request):
    fechaInicio = datetime.date(2025, 7, 7)
    fechaFin = datetime.date(2025, 7, 10)
    comentarios = ComentarioContacto.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/comentarios.html", {"comentarios" :comentarios})

def consultar7(request):
#Consultando entre modelos
    alumnos=Alumnos.objects.filter(comentario__coment__contains='si')
    return render(request,"registros/comentarios.html",{'alumnos':alumnos})

#el de la fecha

def consultar8(request):
    fecha_inicio = datetime.date(2025, 7, 8)
    fecha_fin = datetime.date(2025, 7, 9)
    comentarios = ComentarioContacto.objects.filter(created__range=(fecha_inicio, fecha_fin))
    return render(request, "registros/comentarios.html", {"comentarios": comentarios})

 # exprecion comentario
def consultar9(request):
    expresion = request.GET.get("expresion", "hooa")
    comentarios = ComentarioContacto.objects.filter(mensaje__icontains=expresion)
    return render(request, "registros/comentarios.html", {"comentarios": comentarios})

#el de busqueda de usuario
def consultar10(request):
    comentarios = ComentarioContacto.objects.filter(usuario__exact="julieta")
    return render(request, "registros/comentarios.html", {"comentarios": comentarios})

#
def consultar11(request):
    # Mostrar solo los comentarios que empiecen con una expresión diferente (ejemplo: "soda pop")
    comentarios = ComentarioContacto.objects.filter(mensaje__startswith="ho")
    return render(request, "registros/comentarios.html", {"comentarios": comentarios})


def archivos(request):
    if request.method == 'POST':
            form = FormArchivos(request.POST, request.FILES)
            if form.is_valid():
                titulo = request.POST['titulo']
                descripcion = request.POST['descripcion']
                archivo = request.FILES['archivo']
                insert = Archivos(titulo=titulo, descripcion=descripcion,
                archivo=archivo)
                insert.save()
                return render(request,"registros/archivos.html")
            else:
                messages.error(request, "Error al procesar el formulario")

    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})
