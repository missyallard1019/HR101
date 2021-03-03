from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from ..views import home, education

# Create your tests here.
class HomeTests(TestCase):
	def test_home_view_status_code(self):
		url = reverse('home')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)
		
	def test_home_url_resolves_home_view(self):
		view = resolve('/')
		self.assertEquals(view.func, home)
		
	def test_home_view_contains_link_to_community_url(self):
		home_url = reverse('home')
		response = self.client.get(home_url)
		community_url = reverse('community')
		self.assertContains(response, 'href="{0}"'.format(community_url))
		
	def test_home_view_contains_link_to_education_url(self):
		home_url = reverse('home')
		response = self.client.get(home_url)
		education_url = reverse('education')
		self.assertContains(response, 'href="{0}"'.format(education_url))