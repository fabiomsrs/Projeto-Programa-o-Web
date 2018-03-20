from django import forms
from .models import Livro

class FormLivro(forms.ModelForm):
	class Meta:
		model = Livro		
		fields = '__all__'
