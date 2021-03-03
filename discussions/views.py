from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import NewTopicForm
from .models import Board, Topic, Post

def discussions(request):
    boards = Board.objects.all()

    return render(request, 'community.html', {'boards': boards})

@login_required
def new_topic(request, pk):
	board = get_object_or_404(Board, pk=pk)
	
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.board = board
			topic.starter = request.user
			topic.save()
			post = Post.objects.create(
				message=form.cleaned_data.get('message'),
				topic=topic,
				created_by=request.user
			)
		
			return redirect('community')
		
	else:
		form = NewTopicForm()
		
	return render(request, 'new_topic.html', {'board': board, 'form': form})