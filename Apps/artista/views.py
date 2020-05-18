from django.shortcuts import render , HttpResponse
from .formulario import AlbumForm
from django.contrib import messages
from Apps.Usuarios.models import Album
from Apps.Usuarios.models import Genero
from Apps.Usuarios.models import Disquera
from Apps.Usuarios.models import User
from Apps.Usuarios.models import Cancion
import json
# Create your views here.

def HomeAR(request):
    return render(request, 'home_artista.html')

def Perfil(request):
    datos = User.objects.filter(username=request.user)
    print(datos)
    return render(request,"PerfilUser.html",{
        'datos':datos
    })


def Canciones(request):
    canciones = Cancion.objects.filter(album__artista=request.user).order_by("album")
    print(canciones)
    albums = Album.objects.filter(artista=request.user)
    print(albums)
    return render(request,"Canciones.html",{
        'albums':albums , 'canciones':canciones

    })


def NuevaCancion(request):
    
    # return render(request,"NewCancion.html")
    if request.method == 'POST':
        form = AlbumForm(request.POST,request.FILES)
        
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            duracion = form.cleaned_data['duracion']
            fecha = form.cleaned_data['fecha']
            foto = form.cleaned_data['foto']
            genero = form.cleaned_data['Genero']
            disquera = form.cleaned_data['Disquera']
            
            
            # nombre = Album.objects.filter(nombre=nombre)
            
            

            # if(len(nombre)>0):
            #     form.add_error('nombre','Nombre no Disponible')
            #     return render(request,request,'NewCancion.html',{'form':form})
            
            album = Album(
                nombre = nombre,
                duracion = duracion,
                fecha = fecha,
                foto = foto,
                Genero = genero,
                Disquera = disquera,
                artista = request.user
            
            )
            
            album.save()
            messages.success(request,'Album Creado Exitosamente')
            return render(request,'NewCancion.html',{'form':form})
                
        else:
            return render(request,'NewCancion.html',{'form':form})
    else:
        form = AlbumForm()
        return render(request,'NewCancion.html',{'form':form})    

def EditarCancion(request,idAlbum):
    # album = Album.objects.get(id=idAlbum)
    canciones = Cancion.objects.filter(album__id=idAlbum)
    return render(request,"EditarCancion.html" , {

        'canciones':canciones,
        'idAlbum':idAlbum
    })



def NewPassword(request):
    return render(request,"NewPassword.html")

def actualizarAlbum(request):
    datos  = json.loads(request.body)
    # print(datos)

    idAlbum = int(datos['idAlbum'])
    fechaAlbum = datos['FechaAlbum']
    NombreAlbum = datos['NombreAlbum']
    GeneroAlbum = datos['GeneroALbum']


    try:
        album = Album.objects.get(id=idAlbum)

        album.fecha = fechaAlbum
        album.nombre = NombreAlbum
        

        genero_nuevo , fueCreado = Genero.objects.get_or_create(nombre=GeneroAlbum)
        album.genero =genero_nuevo
        album.save()
        return HttpResponse(True)
    except Exception as identifier: 
        print(identifier)
        return HttpResponse(False)
    

def EliminarAlbum(request) : 
    idAlbum = int(json.loads(request.body))
    print(idAlbum)

   

    try:
        album = Album.objects.get(id=idAlbum)

        album.delete()
        return HttpResponse(True)
    except Exception as identifier:
        print(identifier)
        return HttpResponse(False)
    

def agregarCancion(request):
    nombreCancion = request.POST['nombreCancion']
    duracionCancion = request.POST['duracionCancion']
    autorCancion = request.POST['autorCancion']
    idAlbum = request.POST['idAlbum']
    archivoCancion = request.FILES['archivoCancion']
    print(nombreCancion,duracionCancion,autorCancion,idAlbum,archivoCancion)


    try:
        
        Cancion.objects.create(
         nombre = nombreCancion,
         duracion = duracionCancion,
         autor = autorCancion,
         album_id = idAlbum,
         archivo = archivoCancion
        )
        print("HOLA")
        return HttpResponse(True)
    except Exception as error:
        print(error)
        
        return HttpResponse(False)
