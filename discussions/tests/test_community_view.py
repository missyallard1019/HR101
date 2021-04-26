from django.urls import reverse, resolve
from django.test import TestCase
from django.contrib.auth.models import User
from ..views import discussions
from ..models import Board, Post, Topic
from ..forms import PostForm

class BoardTopicsTests(TestCase):
	def setUp(self):
		Board.objects.create(name='Test Board', description='Board for testing.')
		
	def test_discussions_view_success_status_code(self):
		url = reverse('community')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)
		
	def test_discussions_url_resolves_discussions_view(self):
		view = resolve('/community/')
		self.assertEquals(view.func, discussions)
		
	def test_community_view_contains_navigation_links(self):
		community_url = reverse('community')
		home_url = reverse('home')
		education_url = reverse('education')
		new_topic_url = reverse('new_topic', kwargs={'pk': 1})
		
		response = self.client.get(community_url)
		
		self.assertContains(response, 'href="{0}"'.format(home_url))
		self.assertContains(response, 'href="{0}"'.format(education_url))
		self.assertContains(response, 'href="{0}"'.format(new_topic_url))
		
class ReplyTopicTestCase(TestCase):
	def setUp(self):
		self.board = Board.objects.create(name='Test Board', description='Board for testing.')
		self.username = 'john'
		self.password = '123'
		user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
		self.topic = Topic.objects.create(subject="Hello, world", board=self.board, starter=user)
		Post.objects.create(message="Lorem ipsum dolor sit amet", topic=self.topic, created_by=user)
		self.url = reverse('community')
		
class ReplyTopicTests(ReplyTopicTestCase):
	def setUp(self):
		super().setUp()
		self.client.login(username=self.username, password=self.password)
		self.response = self.client.get(self.url)
		
	def test_csrf(self):
		self.assertContains(self.response, 'csrfmiddlewaretoken')
		
	def test_contains_form(self):
		form = self.response.context.get('form')
		self.assertIsInstance(form, PostForm)
		
	def test_form_inputs(self):
		self.assertContains(self.response, '<input', 3)
		self.assertContains(self.response, '<textarea', 1)
		
class SuccessfulReplyTopicTests(ReplyTopicTestCase):
	def setUp(self):
		super().setUp()
		self.client.login(username=self.username, password=self.password)
		self.repsonse = self.client.post(self.url, {'topic_id': self.topic.id, 'message': "hello, world!"})
		
	def test_reply_created(self):
		self.assertEquals(Post.objects.count(), 2)
		
class InvalidReplyTopicTests(ReplyTopicTestCase):
	def setUp(self):
		super().setUp()
		self.client.login(username=self.username, password=self.password)
		self.response = self.client.post(self.url, {'topic_id': self.topic.id})
		
	def test_status_code(self):
		self.assertEquals(self.response.status_code, 200)
		
	def test_form_errors(self):
		form = self.response. context.get('form')
		self.assertTrue(form.errors)
		