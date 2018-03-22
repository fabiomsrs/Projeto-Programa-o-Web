from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator
from .forms import FormLivro
from .forms import AnuncioFilter
from .models import Anuncio, Livro

# Create your views here.
class Home(View):
	def get(self,request):
		list_anuncio = Anuncio.objects.filter(is_ativo=True)
		
		#campo de busca
		anuncio_filter = AnuncioFilter(request.GET, queryset=list_anuncio)
		
		#paginação
		paginator = Paginator(anuncio_filter.qs, 2)
		page = request.GET.get('page')        
		lista = paginator.get_page(page)
		index = lista.number - 1
		max_index = len(paginator.page_range)
		start_index = index - 3 if index >= 3 else 0
		end_index = index + 3 if index <= max_index - 3 else max_index
		page_range = list(paginator.page_range)[start_index:end_index]

		return render(request, "core/home.html", {'anuncio_filter':anuncio_filter, 'page_range':page_range, 'anuncio_lista':lista})
	
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


class DetalheLivro(View):
	def get(self, request, *args, **kwargs):
		livro_id = self.kwargs['livro_id']
		livro = Livro.objects.get(pk=livro_id)

		return render(request, "core/detalhe_livro.html", {'livro':livro})


class AdquirirLivro(View):
	def get(self, request, *args, **kwargs):
		livro_id = self.kwargs['livro_id']
		request.user.adquirir_livro_doado(livro_id)

		return redirect('core:home')
