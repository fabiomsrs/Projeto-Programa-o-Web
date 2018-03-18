from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
	telefone = models.CharField(max_length=14, verbose_name='Celular')
	email = models.EmailField(null=True, verbose_name='E-mail')	

	def full_name(self):
		return self.__str__()

	def __str__(self):		
		return self.first_name + ' ' + self.last_name

	def save(self, *args, **kwargs):	
		if not self.has_usable_password():	
			self.set_password(self.password)  # password encryption
		super(Usuario, self).save()