from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin

class UsuarioAdmin(UserAdmin):
    fieldsets= UserAdmin.fieldsets + (
        ('Campos Extra', {
            'fields':('is_premium',
            'is_artist',
            'fechaNacimiento',
            'pais',
            'foto',
            )
        }),



    )
# Register your models here.
admin.site.register(User,UsuarioAdmin)
admin.site.register(Cancion)
admin.site.register(Album)
admin.site.register(Playlist)
admin.site.register(Disquera)
admin.site.register(Genero)
admin.site.register(PlaylistCanciones)
admin.site.register(UsuarioCanciones)
