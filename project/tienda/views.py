from django.shortcuts import render
from tienda.forms import  SignupForm

# Create your views here.



def home(request):
     return render(request,'home.html')

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('')

		else:
			return render(request, 'login.html',{'error':'Invalid username and password'})
	

	return render(request,'login.html')


def signup(request):
     if request.method == 'POST':
          form = SignupForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('users:login')

     else:
          form = SignupForm()

     return render(
          request=request,
          template_name = 'signup.html',
          context = {'form': form}
     )