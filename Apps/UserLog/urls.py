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
from Apps.UserLog import views as views_UserLog
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views_UserLog.First,name='First'),
    path('Home',views_UserLog.loginn,name='Home'),
    path('Registro',views_UserLog.Registro,name='Registro'),
    path('CerrarSesion',views_UserLog.cerrarSesion,name='cerrarSesion')
]

urlpatterns += staticfiles_urlpatterns()
