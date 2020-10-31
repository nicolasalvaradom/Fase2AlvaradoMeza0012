from django import forms

from . models import Game, Genre

class GenreForm(forms.ModelForm):
    name = forms.CharField(label='Titulo',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    summary = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    class Meta:
        model = Genre
        fields = ('name', 'summary',)

class GameForm(forms.ModelForm):
    title = forms.CharField(label='Titulo',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    developer = forms.CharField(label='Desarrollador', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    editor = forms.CharField(label='Editor', max_length=100,widget=forms.URLInput(
        attrs={
            'class':'form-control'
        }
    ))
    summary = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), label='Género',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
            ))
    image = forms.ImageField(label='Imagen',
            widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control' 
            }
            ))

             
    class Meta:
        model = Game
        fields = ('title','developer','editor', 'summary', 'genre', 'image',)