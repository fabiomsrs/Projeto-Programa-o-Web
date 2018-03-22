from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import Transacao, Livro, Anuncio
# Create your models here.

class Usuario(AbstractUser):
	telefone = models.CharField(max_length=14, verbose_name='Celular')
	email = models.EmailField(null=True, verbose_name='E-mail')	

	def adquirir_livro_doado(self, livro):		
		livro = Livro.objects.get(pk=livro)
		
		if livro.dono == self:
			if self.is_anonymous():
				raise Exception('Usuario não logado')	
			raise Exception('Você não pode adquirir o proprio livro')

		Transacao.objects.create(emissor=livro.dono,receptor=self,livro=livro)
		anuncio = Anuncio.objects.get(livro=livro)
		anuncio.is_ativo = False
		anuncio.save()

	def full_name(self):
		return self.__str__()

	def __str__(self):		
		return self.first_name + ' ' + self.last_name

	def save(self, *args, **kwargs):	
		if not self.has_usable_password():	
			self.set_password(self.password)  # password encryption
		self.username = self.email
		super(Usuario, self).save()