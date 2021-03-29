from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Chapter, Review, Progress

def home(request):
	return render(request, 'home.html')

def education(request):
	chapter = Chapter.objects.get(index=0)
	
	if request.user.is_authenticated:
		progress = Progress.objects.get(user=request.user)
	else:
		progress = Progress.objects.get(pk=1)
	
	return render(request, 'education.html', {'chapter': chapter, 'progress': progress})

@login_required
def course(request, index):
	if int(index) < 1:
		return redirect('education')
	
	chapter = get_object_or_404(Chapter, index=index)
	reviews = Review.objects.all()
	progress = Progress.objects.get(user=request.user)
	
	return render(request, 'course.html', {'chapter': chapter, 'reviews': reviews, 'progress': progress})

@login_required
def course2(request):
	chapters = Chapter.objects.all()
	reviews = Review.objects.all()
	
	return render(request, 'course2.html', {'chapters': chapters, 'reviews': reviews})