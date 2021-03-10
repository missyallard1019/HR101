from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import NewTopicForm, PostForm, ProfileUpdateForm
from .models import Board, Topic, Post, Profile

def discussions(request):
	boards = Board.objects.all()
	
	if request.method == 'POST':
		form = PostForm(request.POST)
		topic_id_list = request.POST.getlist('topic_id')
		topic_id = topic_id_list[0]
		
		topic = Topic.objects.get(id=topic_id)
		
		if form.is_valid():
			post = form.save(commit=False)
			post.topic = topic
			post.created_by = request.user
			post.save()
			return redirect('community')
	else:
		form = PostForm()
	return render(request, 'community.html', {'boards': boards, 'form': form})


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

@login_required
def profile(request):
	user = request.user
	
	if request.method == 'POST':
		current_profile = Profile.objects.get(user_id=user.id)
		form = ProfileUpdateForm(request.POST, instance=current_profile)
		
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user_id = user.id
			profile.user_type = "Patient"
			profile.save()
			return render(request, 'profile.html')
	else:
		form = ProfileUpdateForm()
		
	return render(request, 'profile.html', {'form': form})