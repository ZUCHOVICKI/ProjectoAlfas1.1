from django.shortcuts import render , HttpResponse

#HttpResponse
#JsonResponse
#Render
# Create your views here.
def HOME(request):
    mensaje = 'Mensaje De HOME en view USUARIOS'
    return render(request,'Usuarios_home.html',{'mensaje':mensaje})
