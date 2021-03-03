from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import SignUpForm

# Create your views here.
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})

def profile(request):
	user = User.objects.all()
	
	return render(request, 'profile.html', {'user': user})