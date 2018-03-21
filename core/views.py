from django.shortcuts import render, redirect
from django.views import View
from .forms import FormLivro
from .forms import AnuncioFilter
from .models import Anuncio

# Create your views here.
class Home(View):
	def get(self,request):
		list_anuncio = Anuncio.objects.all()
		anuncio_filter = AnuncioFilter(request.GET, queryset=list_anuncio)
		return render(request, "core/home.html", {'anuncio_filter':anuncio_filter})
	
class CadastroLivro(View):
	def get(self, request):
		form = FormLivro()	
		return render(request, "core/cadastro.html", {'form':form})

	def post(self, request):		
		form = FormLivro(request.POST)
		
		if form.is_valid():
			livro = form.save(commit=False)		
			if request.FILES:
				livro.foto = request.FILES['foto']
			livro.dono = request.user				
			livro.save()
		else:		
			return render(request, "core/cadastro.html", {'form':form})

		return redirect('core:home')
