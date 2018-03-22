from django import forms
from .models import Livro,Anuncio
import django_filters


class FormLivro(forms.ModelForm):
	class Meta:
		model = Livro		
		fields = '__all__'
		exclude = ['dono']


class AnuncioFilter(django_filters.FilterSet):	
    class Meta:
        model = Anuncio
        fields = ['livro__titulo']
