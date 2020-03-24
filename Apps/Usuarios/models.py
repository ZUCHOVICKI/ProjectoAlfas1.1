from django.db import models
import os
from django.conf import settings


def image_Path():
    return os.path.join(settings.STATICFILES_DIR,'img')
def image_Path_User():
    return os.path.join(settings.STATICFILES_DIR,'UserImg')
# Create your models here.

class Cancion(models.Model):
    nombre = models.CharField(max_length = 50)
    duracion = models.DecimalField(max_digits=4,decimal_places=2)
    autor = models.CharField(max_length = 100 )
    calificacion = models.DecimalField(max_digits=4,decimal_places=2)


class Album(models.Model):
    nombre =  models.CharField(max_length = 50)
    duracion = models.DecimalField(max_digits = 4 , decimal_places = 2)
    fecha = models.DateField(auto_now= False, auto_now_add = False)
    foto = models.ImageField(upload_to =image_Path , max_length=100)

class Usuario(models.Model):
    nombre =  models.CharField(max_length = 60)
    apellidos  =  models.CharField(max_length = 100)
    email =  models.CharField(max_length = 200)
    password =  models.CharField(max_length = 16)
    username =  models.CharField(max_length = 30)
    is_premium = models.BooleanField(default=0)
    fechaNacimiento = models.DateField(auto_now=False,auto_now_add=False)
    pais =  models.CharField(max_length = 30)
    foto = models.ImageField(upload_to = image_Path_User , max_length= 100)
    is_artist =  models.BooleanField(default=0)


class Playlist(models.Model):
    nombre =  models.CharField(max_length = 100)
    Is_public = models.BooleanField(default=0)

class Disquera(models.Model):
    nombre =  models.CharField(max_length = 50)
    duracion = models.CharField(max_length=200)

class Genero(models.Model):
    nombre =  models.CharField(max_length = 50)
    descripcion = models.CharField(max_length=300)
