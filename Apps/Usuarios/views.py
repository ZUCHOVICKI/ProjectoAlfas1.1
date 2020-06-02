from django.shortcuts import render , HttpResponse
from Apps.Usuarios.models import Cancion
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import user_passes_test
# from .formulario import LoginForm
#HttpResponse
#JsonResponse
#Render
# Create your views here.

@login_required
def HomeU(request):
    canciones = Cancion.objects.all().order_by("album")
    return render(request,'Home_usuario.html',{

        'canciones':canciones
    })
#
@login_required
def Inicio(request):
    return render(request,'WelcomeHome.html')

@login_required
def busqueda(request):
    texto = request.POST['texto']

    if texto != "":
        canciones = Cancion.objects.filter(
            Q(nombre__icontains =texto)|
            Q(autor__icontains =texto)|
            Q(album__nombre__icontains =texto)|
            Q(album__Genero__nombre__icontains =texto)|
            Q(album__artista__username__icontains =texto)

        ).values_list('nombre','duracion','autor','album__nombre','archivo').order_by('album')


        lista = list(canciones)
        return JsonResponse({'lista':lista})
    
    else:
        canciones = Cancion.objects.all().values_list('nombre','duracion','autor','album__nombre','archivo').order_by('album')
        lista = list(canciones)
        return JsonResponse({'lista':lista})