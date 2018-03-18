from django.contrib import admin
from .models import Usuario

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):

	search_fields = ['first_name']
	search_fields_hint = 'Buscar pelo nome'
	list_display =('pk','username','full_name','email')

	fieldsets = (
		(None, {
			'fields': ('first_name','last_name','username','password','email','telefone')
		}),
		)
