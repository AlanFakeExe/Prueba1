from django.contrib import admin
from .models import Alumnos
from .models import Comentarios
from .models import ComentarioContacto



class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ("created", "updated")  # Campos que no se pueden editar
    list_display = ("matricula", "nombre", "carrera", "turno")  # Campos a mostrar en la lista
    search_fields = ("matricula", "nombre", "carrera")  # Campos para buscar
    date_hierarchy = "created"  # Permite filtrar por fecha de creación
    list_filter = ('turno', 'carrera')  # Filtro por turno
    list_per_page = 2  # Número de registros por página
    list_display_links = ('matricula', 'nombre')  # Campos que son enlaces a la edición
    list_editable = ('turno',)  # Campos editables directamente en la lista

def get_readonly_fields(self, request, obj=None):
    if request.user.groups.filter(name='Usuarios').exists():
        return ('created', 'updated', 'matricula', 'nombre', 'carrera', 'turno')
    else:
        return ('created', 'updated')

admin.site.register(Alumnos, AdministrarModelo)

class AdministradorComentarios(admin.ModelAdmin):
    list_display = ("id", "coment")
    search_fields = ("id", "created")
    date_hierarchy = "created"

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="eliminar").exists():
            return ('created', 'id', 'alumno') 
        else:
            return ('created', 'id', 'alumno') 

admin.site.register(Comentarios, AdministradorComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="eliminar").exists():
            return ('created', 'id', 'mensaje')  
        else:
            return ('created', 'id')


admin.site.register(ComentarioContacto, AdministrarComentariosContacto)

