from django.shortcuts import render , HttpResponse , redirect
from .formulario import LoginForm,RegisterForm
from django.contrib.auth import authenticate , login
from Apps.Usuarios import views as views_Usuarios
from django.contrib.auth.models import User
from django.contrib import messages
#HttpResponse
#JsonResponse
#Render
# Create your views here.
def loginn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username = username , password = password)
            if user is not None:
                login(request,user)
                return redirect(views_Usuarios.Home)
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
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            Nombre = form.cleaned_data['first_name']
            Apellido = form.cleaned_data['last_name']

            user , created = User.objects.get_or_create(
            username = username,
            email = email
            )
            if created:
                messages.success(request,'Usuario Creado Exitosamente')
                return render(request,'Registro.html',{'form':form})
            else:
                return render(request,'Registro.html',{'form':form})
        else:
            return render(request,'Registro.html',{'form':form})
    else:
        form = RegisterForm()
        return render(request,'Registro.html',{'form':form})
