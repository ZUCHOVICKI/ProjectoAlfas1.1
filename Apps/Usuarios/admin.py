from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Cancion)
admin.site.register(Album)
admin.site.register(Playlist)
admin.site.register(Disquera)
admin.site.register(Genero)
admin.site.register(PlaylistCanciones)
admin.site.register(UsuarioCanciones)
