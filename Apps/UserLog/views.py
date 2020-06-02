from django.shortcuts import render , HttpResponse , redirect
from .formulario import LoginForm,RegisterForm
from django.contrib.auth import authenticate , login , logout
from Apps.Usuarios import views as views_Usuarios
from Apps.artista import views as views_artista
# from django.contrib.auth.models import User
from django.contrib import messages
from Apps.Usuarios.models import User
#HttpResponse
#JsonResponse
#Render
# Create your views here.
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import user_passes_test


def First(request):

    if(request.user.is_authenticated):
        if(request.user.is_artist):

            return redirect(views_artista.HomeAR)

        else:
            return redirect(views_Usuarios.HomeU)
    else:
        return render(request,'WelcomeHome.html')

        
def loginn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username = username , password = password)
            if user is not None:
                login(request,user)
                if(user.is_artist):
                    return redirect(views_artista.HomeAR)
                else:
                    return redirect(views_Usuarios.HomeU)
            else:
                form.add_error(None,'Datos Incorrectos ==> Revisa tus datos')
                # form = LoginForm()

                return render(request,'login.html',{'form':form})


        else:
            return HttpResponse('Revisa tu formulario')
    else:
        form = LoginForm()

        return render(request,'login.html',{'form':form})



def Registro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            Nombre = form.cleaned_data['first_name']
            Apellido = form.cleaned_data['last_name']
            fechaNacimiento = form.cleaned_data['fechaNacimiento']
            pais = form.cleaned_data['pais']
            foto = form.cleaned_data['foto']
            is_artist  =form.cleaned_data['is_artist']

            user = User.objects.filter(username=username)
            emailUser = User.objects.filter(email=email)

            if(len(user)>0):
                form.add_error('username','Usuario no Disponible')
                return render(request,request,'Registro.html',{'form':form})
                

            if(len(emailUser)>0):
                form.add_error('email','Correo no Disponible')
                return render(request,'Registro.html',{'form':form})
                


            user = User(
                username = username,
                email = email,
                first_name = Nombre,
                last_name = Apellido,
                fechaNacimiento = fechaNacimiento,
                pais = pais,
                foto = foto,
                is_artist = is_artist
            )
            user.set_password(password)  
            user.save()
            messages.success(request,'Usuario Creado Exitosamente')
            return render(request,'Registro.html',{'form':form})
            
        else:
            return render(request,'Registro.html',{'form':form})
    else:
        form = RegisterForm()
        return render(request,'Registro.html',{'form':form})

@login_required
def cerrarSesion(request):
    logout(request)
    return redirect(First)
    

#########################