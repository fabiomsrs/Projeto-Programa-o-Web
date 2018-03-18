from django.db import models

# Create your models here.

class Livro(models.Model):
	NIVEL_CONSERVACAO = (
        ('ruim', 'Ruim'),
        ('razoavel', 'Razoavel'),
        ('bom', 'Bom'),
        ('excelente', 'Excelente')
    )

	titulo = models.CharField(max_length=45)
	autor = models.CharField(max_length=75)
	edicao = models.CharField(max_length=10)
	genero = models.ManyToManyField('Genero')
	nivel_conservacao = models.CharField(max_length=45, choices=NIVEL_CONSERVACAO)
	dono = models.ForeignKey('user.Usuario', on_delete=models.CASCADE,related_name='meus_livros')


class Transacao(models.Model):
	emissor = models.ForeignKey('user.Usuario', on_delete=models.CASCADE,related_name='livros_desapegados')
	receptor = models.ForeignKey('user.Usuario', on_delete=models.CASCADE,related_name='livros_adiquiridos')
	livro = models.OneToOneField('Livro', on_delete=models.CASCADE,related_name='minha_transacao')	


class Anuncio(models.Model):
	livro = models.OneToOneField('Livro', on_delete=models.CASCADE,related_name='meu_anuncio')
	data_anuncio = models.DateTimeField(auto_now=True)
	foto = models.ImageField(upload_to='img/')
	is_ativo = models.BooleanField(default=True)
	is_doacao = models.BooleanField(default=True)

	@property
	def dono(self):
		return self.livro.dono

class Genero(models.Model):
	nome = models.CharField(max_length=25)

	def __str__(self):
		return self.nome