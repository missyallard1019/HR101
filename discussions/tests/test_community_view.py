from django.urls import reverse, resolve
from django.test import TestCase
from ..views import discussions
from ..models import Board

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
		