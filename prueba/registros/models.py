from django.db import models
from ckeditor.fields import RichTextField  # Importa el campo RichTextField de CKEditor
from django.db import models

class Alumnos(models.Model):  # Define la estructura de nuestra tabla
    matricula = models.CharField(max_length=12, verbose_name="Mat")  # Texto corto
    nombre = models.TextField()  # Texto largo
    carrera = models.TextField()
    imagen = models.ImageField( null=True,upload_to="fotos", verbose_name="Fotografias")  # Imagen, null=True permite que el campo sea opcional
    turno = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación
    updated = models.DateTimeField(auto_now=True)  # Fecha y hora de última actualización

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]  # Ordena del más reciente al más viejo

    def __str__(self):
        return self.nombre  # Retorna el nombre como representación del objeto
    # models.py
        foto = models.ImageField(upload_to='fotos/')
    # otros campos...

class Comentarios(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE, verbose_name="Alumno")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    coment = models.TextField(verbose_name="Comentario")
    coment = RichTextField(verbose_name="Comentario con formato")  # Campo de texto enriquecido
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created"]
    def __str__(self):
        return self.coment
    
class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    usuario = models.TextField(verbose_name="Usuario")
    mensaje = models.TextField(verbose_name="Comentario")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")

    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]

    def __str__(self):
        return self.mensaje
    
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre
    
class Archivos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    archivo = models.FileField(upload_to="archivos",
    null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"
        ordering = ["-created"]

    def __str__(self):
     return self.titulo

class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    usuario = models.TextField(verbose_name="Usuario")
    mensaje = models.TextField(verbose_name="Comentario")
    created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]

    def __str__(self):
        return self.mensaje