from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import NewTopicForm, PostForm, ProfileUpdateForm
from .models import Board, Topic, Post, Profile

def discussions(request):
	boards = Board.objects.all()

	if request.method == 'POST':
		post_id = request.POST.get('post_id')
	
		if post_id == None:
			form = PostForm(request.POST, auto_id=False)
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
			current_post = Post.objects.get(id=post_id)
			form = PostForm(request.POST or None, instance=current_post, auto_id=False)
			
			if form.is_valid():
				form.save()
				return redirect('community')

	else:
		form = PostForm(auto_id=False)
	
	return render(request, 'community.html', {'boards': boards, 'form': form})

def search(request):
	results = []
	posts = Post.objects.all()
	boards = Board.objects.all()
	topics = Topic.objects.all()
	query = request.GET.get('q')
	
	board_results1 = Board.objects.filter(name__contains=query)
	for b in board_results1:
		results.append(b)
	board_results2 = Board.objects.filter(description__contains=query)
	for c in board_results2:
		results.append(c)

	topic_results = Topic.objects.filter(subject__icontains=query)
	for t in topic_results:
		if t in results:
			print("already exists")
		else:
			results.append(t)

	post_results = Post.objects.filter(message__icontains=query)
	for p in post_results:
		p_topic = p.topic
		if p_topic in results:
			print("already exists")
		else:
			results.append(p_topic)

	if request.method == 'POST':
		post_id = request.POST.get('post_id')
		if post_id == None:
			form = PostForm(request.POST, auto_id=False)
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
			current_post = Post.objects.get(id=post_id)
			form = PostForm(request.POST or None, instance=current_post)
			
			if form.is_valid():
				form.save()
				return redirect('community')
	else:
		form = PostForm(auto_id=False)
		
	return render(request, 'search_results.html', {'results': results, 'query': query, 'boards': boards, 'posts': posts, 'topics': topics, 'form': form})


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
	user_topics = []
	user_posts_topics = []
	
	for topic in Topic.objects.all():
		if topic.starter == user:
			user_topics.append(topic)
	
	for post in Post.objects.all():
		if post.topic.starter == user:
			pass
		elif post.created_by == user:
			if post.topic in user_posts_topics:
				pass
			else:
				user_posts_topics.append(post.topic)
	
	current_profile = Profile.objects.get(user_id=user.id)
	form = ProfileUpdateForm(request.POST or None, instance=current_profile)


	if form.is_valid():
		profile = form.save(commit=False)
		profile.user_id = user.id
		profile.user_type = "Patient"
		profile.save()
		return redirect('profile')
		
	return render(request, 'profile.html', {'form': form, 'user_topics': user_topics, 'user_posts_topics': user_posts_topics})