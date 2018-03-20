from django.shortcuts import render, redirect
from django.views import View
from .forms import FormLivro

# Create your views here.
class Home(View):
	def get(self,request):
		return render(request, "home.html")
	
class CadastroLivro(View):
	def get(self, request):
		form = FormLivro()
		return render(request, "cadastro.html", {'form':form})

	def post(self, request):		
		form = FormLivro(request.POST)
		
		if form.is_valid():
			livro = form.save(commit=False)		
			if request.FILES:
				livro.foto = request.FILES['foto']				
			livro.save()
		else:		
			return render(request, "cadastro.html", {'form':form})

		return redirect('core:home')
