from django import forms
from django.forms import ModelForm
from Apps.Usuarios.models import Album
from Apps.Usuarios.models import Genero
class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['nombre','duracion','fecha','foto','Genero','Disquera']
        widgets = {
        'nombre' :forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Del Album'} ),
        'duracion':forms.NumberInput(attrs={'class':'form-control','placeholder':'Duracion del Album'}),
        'fecha' : forms.DateInput(format ='%d/%m/%y',attrs={'class':'form-control','placeholder':'Fecha de Publicacion'}),
        'foto' :forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Foto del Album'} ),
        'Genero':forms.TextInput(attrs={'class':'form-control','placeholder':'Genero del Album'}),
        'Disquera' : forms.TextInput(attrs={'class':'form-control','placeholder':'Disquera del Album'})


        }
        help_texts = {
        'Genero':Genero.objects.all(),
        'password':'Maximo 8 Caracteres'

        }
        
        #  publication = forms.ChoiceField(
        # choices=[(x.id,x.name) for x in Publication.objects.all()]
        #  )