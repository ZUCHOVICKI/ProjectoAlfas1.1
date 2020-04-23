from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from Apps.Usuarios.models import User
def image_Path():
    return os.path.join(settings.STATICFILES_DIR,'img')
def image_Path_User():
    return os.path.join(settings.STATICFILES_DIR,'UserImg')
# Create your models here.

class Cancion(models.Model):
    nombre = models.CharField(max_length = 50)
    duracion = models.DecimalField(max_digits=4,decimal_places=2)
    autor = models.CharField(max_length = 100 )
    calificacion = models.DecimalField(max_digits=4,decimal_places=2 , null = True,blank = True)
    album = models.ForeignKey('Album',on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.nombre , self.album)

    class Meta:
        verbose_name = "Cancion"
        verbose_name_plural = "Canciones"


class Album(models.Model):
    nombre =  models.CharField(max_length = 50)
    duracion = models.DecimalField(max_digits = 4 , decimal_places = 2, null = True ,blank = True)
    fecha = models.DateField(auto_now= False, auto_now_add = False)
    foto = models.ImageField(upload_to =image_Path , max_length=100, null = True ,blank = True)
    Genero = models.ForeignKey('Genero',on_delete=models.CASCADE)
    Disquera = models.ForeignKey('Disquera',on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self):
        return self.nombre


class User(AbstractUser):

    PAISES = [

        ('MX','Mexico')
        , ('EU','Estados Unidos')
    ]


    is_premium = models.BooleanField(default=False,null=False,blank=False)
    fechaNacimiento = models.DateField(auto_now = False , auto_now_add = False,null=True,blank=True)
    pais = models.CharField(max_length = 2, choices = PAISES,null=False,blank=False)
    foto = models.ImageField(upload_to=image_Path_User,null=True,blank=True)
    is_artist = models.BooleanField(default=False,null=False,blank=False)
# class Usuario(models.Model):
#     nombre =  models.CharField(max_length = 60)
#     apellidos  =  models.CharField(max_length = 100, null= True)
#     email =  models.CharField(max_length = 200, null= True)
#     password =  models.CharField(max_length = 16)
#     username =  models.CharField(max_length = 30)
#     is_premium = models.BooleanField(default=0)
#     fechaNacimiento = models.DateField(auto_now=False,auto_now_add=False, null= True)
#     pais =  models.CharField(max_length = 30)
#     foto = models.ImageField(upload_to = image_Path_User , max_length= 100, null= True)
#     is_artist =  models.BooleanField(default=0)


class Playlist(models.Model):
    nombre =  models.CharField(max_length = 100)
    Is_public = models.BooleanField(default=0)
    Usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Playlist"
        verbose_name_plural = "Playlist"
    def __str__(self):
        return "{}-{}".format(self.nombre , self.Usuario)

class Disquera(models.Model):
    nombre =  models.CharField(max_length = 50)
    direccion = models.CharField(max_length=200 , null= True,blank = True)
    class Meta:
        verbose_name = "Disquera"
        verbose_name_plural = "Disqueras"
    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre =  models.CharField(max_length = 50)
    descripcion = models.CharField(max_length=300)
    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"
    def __str__(self):
        return self.nombre


class PlaylistCanciones(models.Model):
    playlist = models.ForeignKey('Playlist',on_delete=models.CASCADE)
    cancion = models.ForeignKey('Cancion',on_delete=models.CASCADE)
    class Meta:
        verbose_name = "PlaylistCanciones"
        verbose_name_plural = "Playlist/Canciones"


class UsuarioCanciones(models.Model):
    Cancion = models.ForeignKey('Cancion',on_delete=models.CASCADE)
    Usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name = "UsuarioCanciones"
        verbose_name_plural = "Usuarios/Canciones"
