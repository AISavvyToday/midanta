from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.





def RegisterView(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		if password1 == password2:
			user = User.objects.create_user(username=username, email=email,password=password1)
			# login(request, user)
			return redirect('login')
		else:
			messages.error(request, 'passwords do not match')


	return render(request, 'accounts/register.html')


def LogInView(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			print(username, password)
			login(request, user)
			messages.success(request, 'You have successfully logged in as {}'.format(username))
			return redirect('home')
		else:
			messages.error(request, 'Invalid username or password, please try again!')

	return render(request, 'accounts/login.html')



def LogOutView(request):
	logout(request)
	messages.success(request, 'Successfully logged out!')
	return redirect('home')