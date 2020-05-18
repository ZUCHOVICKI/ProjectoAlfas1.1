"""DJANGOA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Apps.artista import views as views_artista
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views_artista.HomeAR,name='Home_AR'),
    path('Perfil',views_artista.Perfil,name='Perfil'),
    path('Canciones',views_artista.Canciones,name='Canciones'),
    path('NuevaCancion',views_artista.NuevaCancion,name='NuevaCancion'),
    path('EditarCancion/<int:idAlbum>',views_artista.EditarCancion,name='EditarCancion'),
    path('ActualizarAlbum',views_artista.actualizarAlbum,name='actualizarAlbum'),
    path('delete',views_artista.EliminarAlbum,name='EliminarAlbum'),
    path('AddCancion',views_artista.agregarCancion,name='agregarCancion'),
    path('NewPassword',views_artista.NewPassword,name='NewPassword')
]

urlpatterns += staticfiles_urlpatterns()