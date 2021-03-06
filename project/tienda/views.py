from django.shortcuts import render,redirect
from tienda.forms import  SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def logout_view(request):
	logout(request)
	return redirect('login')

def home(request):
     return render(request,'home.html')

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('home')

		else:
			return render(request, 'login.html',{'error':'Invalid username and password'})
	

	return render(request,'login.html')


def signup(request):
     if request.method == 'POST':
          form = SignupForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('login')

     else:
          form = SignupForm()

     return render(
          request=request,
          template_name = 'signup.html',
          context = {'form': form}
     )
def reclamo(request):
     return render(request,'reclamo.html')     