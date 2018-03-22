from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator
from .forms import FormLivro
from .forms import AnuncioFilter
from .models import Anuncio
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(View):
	def get(self,request):
		list_anuncio = Anuncio.objects.all()
		
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

	
class CadastroLivro(LoginRequiredMixin, View):
	login_url = 'user/login/'

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
