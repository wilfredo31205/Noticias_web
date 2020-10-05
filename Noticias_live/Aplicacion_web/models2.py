from django.db import models

class Autor(models.Model):
    estado = models.BooleanField()
    fecha_creacion = models.DateField()
    fecha_eliminacion = models.DateField()
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=120)
    email = models.CharField(max_length=200)
    descripcion = models.TextField()
    web = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(db_column='Twitter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    instagram = models.CharField(db_column='Instagram', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fecha_modificacion = models.DateField()

    class Meta:
        managed = False
        db_table = 'Aplicacion_web_autor'


class Categoria3(models.Model):
    estado = models.BooleanField()
    fecha_creacion = models.DateField()
    fecha_eliminacion = models.DateField()
    nombre = models.CharField(unique=True, max_length=100)
    imagen_referencial = models.CharField(max_length=100)
    fecha_modificacion = models.DateField()

    class Meta:
        managed = False
        db_table = 'Aplicacion_web_categoria3'