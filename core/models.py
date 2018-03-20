from django.db import models
from datetime import datetime

# Create your models here.

class Livro(models.Model):
	NIVEL_CONSERVACAO = (
        ('ruim', 'Ruim'),
        ('razoavel', 'Razoavel'),
        ('bom', 'Bom'),
        ('excelente', 'Excelente')
    )

	foto = models.ImageField(upload_to='img/', null=True)
	titulo = models.CharField(max_length=45)
	autor = models.CharField(max_length=75)
	edicao = models.CharField(max_length=10)
	genero = models.ManyToManyField('Genero')
	nivel_conservacao = models.CharField(max_length=45, choices=NIVEL_CONSERVACAO)
	dono = models.ForeignKey('user.Usuario', on_delete=models.CASCADE,related_name='meus_livros')
	is_doacao = models.BooleanField(default=True)


class Transacao(models.Model):
	emissor = models.ForeignKey('user.Usuario', on_delete=models.CASCADE,related_name='livros_desapegados')
	receptor = models.ForeignKey('user.Usuario', on_delete=models.CASCADE,related_name='livros_adiquiridos')
	livro = models.OneToOneField('Livro', on_delete=models.CASCADE,related_name='minha_transacao')	
	data_transacao = models.DateField(auto_now=True)

	def checar_livro(self):
		#checar se o livro ja foi doado ou trocado
		if Transacao.objects.filter(livro=self.livro):
			raise ValidationError('Livro ja negociado')	

	def checar_usuario_receptor(self):
		#checar se o usuario recebeu 3 doações no mês se sim, raise execption
		if self.livro.is_doacao:
			if Transacao.objects.filter(receptor=self.receptor).filter(data_transacao__month=
				datetime.now().month).filter(data_transacao__year=datetime.now().year).count() >= 3:
				raise ValidationError('Ja recebeu 3 doações de livros esse mês')		

	def clean(self):		
		super(Transacao, self).clean()
		self.checar_livro()
		self.checar_usuario_receptor()

	def save(self, **kwargs):
		self.clean()
		super(Transacao, self).save()


class Anuncio(models.Model):
	livro = models.OneToOneField('Livro', on_delete=models.CASCADE,related_name='meu_anuncio')
	data_anuncio = models.DateTimeField(auto_now=True)	
	is_ativo = models.BooleanField(default=True)

	@property
	def dono(self):
		return self.livro.dono

class Genero(models.Model):
	nome = models.CharField(max_length=25)

	def __str__(self):
		return self.nome