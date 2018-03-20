from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FormUsuario

# Create your views here.
class Login(View):
	def get(self,request):
		form = AuthenticationForm()
		return render(request, "index.html", {'form':form})

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
		    login(request, user)
		    return redirect('core:home')
		else:
		    return HttpResponse("<h1>LOGIN ERROR</h1>")

class CadastroUsuario(View):
	def get(self,request):
		form = FormUsuario()
		return render(request, "cadastro.html", {'form':form})

	def post(self,request):
		form = FormUsuario(request.POST)
		
		if form.is_valid():
			form.save()		
		else:
			return render(request, "cadastro.html", {'form':form})

		return redirect('user:login')