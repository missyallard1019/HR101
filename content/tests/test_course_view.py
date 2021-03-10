from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from ..views import home, education, course

class LoginRequiredCourseTests(TestCase):
	def setUp(self):
		self.url = reverse('course')
		self.response = self.client.get(self.url)
		
	def test_redirection(self):
		login_url = reverse('login')
		self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))

class CourseTests(TestCase):
	def setUp(self):
		User.objects.create_user(username='john', email='john@doe.com', password='123')
		self.client.login(username='john', password='123')
		
	def test_course_view_status_code(self):
		url = reverse('course')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)
		
	def test_course_url_resolves_course_view(self):
		view = resolve('/course/')
		self.assertEquals(view.func, course)
		
	def test_course_view_contains_link_to_home_url(self):
		course_url = reverse('course')
		response = self.client.get(course_url)
		home_url = reverse('home')
		self.assertContains(response, 'href="{0}"'.format(home_url))
		
	def test_course_view_contains_link_to_community_url(self):
		course_url = reverse('course')
		response = self.client.get(course_url)
		community_url = reverse('community')
		self.assertContains(response, 'href="{0}"'.format(community_url))
		
	def test_course_view_contains_link_to_education_url(self):
		course_url = reverse('course')
		response = self.client.get(course_url)
		education_url = reverse('education')
		self.assertContains(response, 'href="{0}"'.format(education_url))
		
	def test_course_view_contains_link_to_profile_url(self):
		course_url = reverse('course')
		response = self.client.get(course_url)
		profile_url = reverse('profile')
		self.assertContains(response, 'href="{0}"'.format(profile_url))