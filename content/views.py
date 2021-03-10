from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Chapter, Review

def home(request):
	return render(request, 'home.html')

def education(request):
	chapters = Chapter.objects.all()
	
	return render(request, 'education.html', {'chapters': chapters})

@login_required
def course(request):
	chapters = Chapter.objects.all()
	reviews = Review.objects.all()
	
	return render(request, 'course.html', {'chapters': chapters, 'reviews': reviews})

@login_required
def course2(request):
	chapters = Chapter.objects.all()
	reviews = Review.objects.all()
	
	return render(request, 'course2.html', {'chapters': chapters, 'reviews': reviews})