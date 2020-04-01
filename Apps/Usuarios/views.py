from django.shortcuts import render , HttpResponse
# from .formulario import LoginForm
#HttpResponse
#JsonResponse
#Render
# Create your views here.
def Home(request):
    return render(request,'Home_usuario.html')
#
