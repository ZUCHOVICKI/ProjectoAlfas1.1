from django.shortcuts import render , HttpResponse
from .formulario import AlbumForm
from django.contrib import messages
from Apps.Usuarios.models import Album
from Apps.Usuarios.models import Genero
from Apps.Usuarios.models import Disquera
from Apps.Usuarios.models import User
from Apps.Usuarios.models import Cancion
import json
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import user_passes_test

# Create your views here.
@login_required
@user_passes_test(lambda user:user.isArtist()==True)

def HomeAR(request):
    
    return render(request, 'home_artista.html')

@login_required
@user_passes_test(lambda user:user.isArtist()==True)

def Perfil(request):
    datos = User.objects.filter(username=request.user)
    print(datos)
    return render(request,"PerfilUser.html",{
        'datos':datos
    })

@login_required
@user_passes_test(lambda user:user.isArtist()==True)

def Canciones(request):
    todos_albums = Album.objects.filter(artista = request.user).values('id')
    albums_con_canciones = Cancion.objects.filter(album__artista=request.user).values('album')
    albums_sin_canciones = todos_albums.filter(~Q(id__in=albums_con_canciones))
    albums = Album.objects.filter(id__in=albums_sin_canciones)

    print(albums)

    canciones = Cancion.objects.filter(album__artista=request.user).order_by("album")
    print(canciones)
    # albums = Album.objects.filter(artista=request.user)
    # print(albums)
    return render(request,"Canciones.html",{
        'albums':albums , 'canciones':canciones


    })

@login_required
@user_passes_test(lambda user:user.isArtist()==True)

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

@login_required
@user_passes_test(lambda user:user.isArtist()==True)

def EditarCancion(request,idAlbum):
    # album = Album.objects.get(id=idAlbum)
    album = Album.objects.get(id=idAlbum)
    canciones = Cancion.objects.filter(album__id=idAlbum)
    return render(request,"EditarCancion.html" , {

        'canciones':canciones,
        'idAlbum':idAlbum,
        'album':album
    })


@login_required
@user_passes_test(lambda user:user.isArtist()==True)

def NewPassword(request):
    return render(request,"NewPassword.html")

@login_required
@user_passes_test(lambda user:user.isArtist()==True)

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


@login_required    
@user_passes_test(lambda user:user.isArtist()==True)

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


@login_required
@user_passes_test(lambda user:user.isArtist()==True)

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


@login_required
@user_passes_test(lambda user:user.isArtist()==True)

def eliminarCancion(request):
    
    try:
        idCancion = request.POST['idCancion']
        cancion = Cancion.objects.get(id=idCancion)
        cancion.delete()

        return HttpResponse(True)
        
    except Exception as error:
        
        print(error)
        return HttpResponse("Ha Ocurrido un error al eliminar la cancion")


@login_required
@user_passes_test(lambda user:user.isArtist()==True)

def actualizarCancion(request):
    try:
        idCancion = request.POST['idCancion']
        cancion= Cancion.objects.get(id=idCancion)
        cancion.nombre = request.POST['nombreCancion']
        cancion.autor = request.POST['autorCancion']
        cancion.save()

        return HttpResponse(True)
        
    except Exception as error:
        
        print(error)
        return HttpResponse("Ha Ocurrido un error al Actualizar la cancion")

@login_required
@user_passes_test(lambda user:user.isArtist()==True)

def agregarAlbum(request):

   try:
       nombreAlbum = request.POST['nombreAlbum']
       fechaAlbum =request.POST['fechaAlbum']
       disqueraAlbum = request.POST['disqueraAlbum']
       generoAlbum = request.POST['generoAlbum']
       fotoAlbum = request.FILES['fotoAlbum']
       numeroCanciones = int(request.POST['numeroCanciones'])+1

       canciones = []
 
       for x in range(0,numeroCanciones):
           numero = str(x)
           canciones.append(request.FILES['cancion['+numero+']'])

           

       genero,createdGenero = Genero.objects.get_or_create(nombre= generoAlbum)
       disquera, createdDisquera = Disquera.objects.get_or_create(nombre= disqueraAlbum)

       album_nuevo = Album.objects.create(

        nombre = nombreAlbum,
        fecha = fechaAlbum,
        foto = fotoAlbum,
        Genero = genero,
        Disquera = disquera,
        artista = request.user

        )

       for cancion in canciones: 
            name = cancion.name
            name = name.split(".")[0]
            Cancion.objects.create(

                nombre = name,
                duracion = 1.00,
                autor = "Autor anonimo",
                album = album_nuevo,
                archivo = cancion
             )

       return HttpResponse(True)

   except Exception as error:
       print("ERROR = ")
       print(error)
       return HttpResponse(False)
    

    # nombreAlbum = request.POST['nombreAlbum']
    # fechaAlbum =request.POST['fechaAlbum']
    # disqueraAlbum = request.POST['disqueraAlbum']
    # generoAlbum = request.POST['generoAlbum']
    # fotoAlbum = request.FILES['fotoAlbum']
    # numeroCanciones = int(request.POST['numeroCanciones'])+1

    # canciones = []

    # for x in range(0,numeroCanciones):
    #     numero = str(x)
    #     canciones.append(request.FILES['cancion['+numero+']'])

        

    # genero,createdGenero = Genero.objects.get_or_create(nombre= generoAlbum)
    # disquera, createdDisquera = Disquera.objects.get_or_create(nombre= disqueraAlbum)

    # album_nuevo = Album.objects.create(

    # nombre = nombreAlbum,
    # fecha = fechaAlbum,
    # foto = fotoAlbum,
    # genero = genero,
    # disquera = disquera,
    # artista = request.user

    # )

    # for cancion in canciones: 
    #     name = cancion.name
    #     name = name.split(".")[0]
    #     Cancion.objects.create(

    #         nombre = name,
    #         duracion = 1.00,
    #         autor = "Autor anonimo",
    #         album = album_nuevo,
    #         archivo = cancion
    #         )

    # return HttpResponse(True)


