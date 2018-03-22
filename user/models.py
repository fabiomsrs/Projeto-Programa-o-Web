from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import Transacao, Livro, Anuncio
from datetime import datetime
# Create your models here.

class Usuario(AbstractUser):
	telefone = models.CharField(max_length=14, verbose_name='Celular')
	email = models.EmailField(null=True, verbose_name='E-mail')	

	def adquirir_livro_doado(self, livro):		
		livro = Livro.objects.get(pk=livro)		

		Transacao.objects.create(emissor=livro.dono,receptor=self,livro=livro)
		anuncio = Anuncio.objects.get(livro=livro)
		anuncio.is_ativo = False
		anuncio.save()

	def livros_doado_no_mes(self):
		return self.meus_livros.filter(meu_anuncio__data_anuncio__month=datetime.now().month).filter(meu_anuncio__data_anuncio__year=
			datetime.now().year).count()

	def full_name(self):
		return self.__str__()

	def __str__(self):		
		return self.first_name + ' ' + self.last_name

	def save(self, *args, **kwargs):	
		if not self.has_usable_password():	
			self.set_password(self.password)  # password encryption
		self.username = self.email
		super(Usuario, self).save()