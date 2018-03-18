from django.contrib import admin
from .models import Livro

# Register your models here.

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):

	search_fields = ['titulo']
	search_fields_hint = 'Buscar pelo nome'
	list_display =('pk','titulo','nivel_conservacao','dono')
	list_filter = ('genero__nome','autor')
