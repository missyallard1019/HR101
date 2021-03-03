from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from ..views import home, education

class EducationTests(TestCase):
	def test_education_view_status_code(self):
		url = reverse('education')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)
		
	def test_education_url_resolves_education_view(self):
		view = resolve('/education/')
		self.assertEquals(view.func, education)
		
	def test_education_view_contains_link_to_home_url(self):
		education_url = reverse('education')
		response = self.client.get(education_url)
		home_url = reverse('home')
		self.assertContains(response, 'href="{0}"'.format(home_url))
		
	def test_education_view_contains_link_to_community_url(self):
		education_url = reverse('education')
		response = self.client.get(education_url)
		community_url = reverse('community')
		self.assertContains(response, 'href="{0}"'.format(community_url))