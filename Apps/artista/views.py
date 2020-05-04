from django.shortcuts import render

# Create your views here.

def HomeAR(request):
    return render(request, 'home_artista.html')