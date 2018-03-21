from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FormUsuario

# Create your views here.
class Login(View):
	def get(self,request):
		form = AuthenticationForm()
		return render(request, "core/login.html", {'form':form})

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
		    login(request, user)
		    return redirect('core:home')
		else:
		    return HttpResponse("<h1>LOGIN ERROR</h1>")

class Logout(View):
	def get(self,request):
		logout(request)
		return redirect('core:home')


class CadastroUsuario(View):
	def get(self,request):
		form = FormUsuario()
		return render(request, "core/cadastro.html", {'form':form})

	def post(self,request):
		form = FormUsuario(request.POST)
		
		if form.is_valid():
			user = form.save()			 	
			login(request, user)			
		else:
			return render(request, "core/cadastro.html", {'form':form})

		return redirect('core:home')