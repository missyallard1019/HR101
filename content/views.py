from django.shortcuts import render
from .models import Chapter

def home(request):
	return render(request, 'home.html')

def education(request):
	chapters = Chapter.objects.all()
	
	return render(request, 'education.html', {'chapters': chapters})

def course(request):
	chapters = Chapter.objects.all()
	
	return render(request, 'course.html', {'chapters': chapters})

