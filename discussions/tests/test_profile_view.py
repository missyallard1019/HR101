from django.urls import reverse, resolve
from django.test import TestCase
from django.contrib.auth.models import User
from ..views import profile
from ..models import Profile
from ..forms import ProfileUpdateForm

class LoginRequiredProfileTests(TestCase):
	def setUp(self):
		user = User.objects.create_user(username='john', email='john@doe.com', password='123')
		self.url = reverse('profile')
		self.response = self.client.get(self.url)
		
	def test_redirection(self):
		login_url = reverse('login')
		self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))

class ProfileTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='john', email='john@doe.com', password='123')
		self.url = reverse('profile')
		self.response = self.client.get(self.url)
		self.client.login(username='john', password='123')
		
	def test_profile_view_success_status_code(self):
		url = reverse('profile')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)
		
	def test_profile_url_resolves_profile_view(self):
		view = resolve('/profile/')
		self.assertEquals(view.func, profile)
		
	def test_profile_view_contains_link_back_to_community_view(self):
		profile_url = reverse('profile')
		community_url = reverse('community')
		response = self.client.get(profile_url)
		self.assertContains(response, 'href="{0}"'.format(community_url))
		
	def test_profile_view_contains_link_back_to_home_view(self):
		profile_url = reverse('profile')
		home_url = reverse('home')
		response = self.client.get(profile_url)
		self.assertContains(response, 'href="{0}"'.format(home_url))
		
	def test_profile_view_contains_link_back_to_education_view(self):
		profile_url = reverse('profile')
		education_url = reverse('education')
		response = self.client.get(profile_url)
		self.assertContains(response, 'href="{0}"'.format(education_url))
		
	def test_csrf(self):
		url = reverse('profile')
		response = self.client.get(url)
		self.assertContains(response, 'csrfmiddlewaretoken')
		
	def test_profile_valid_post_data(self):
		url = reverse('profile')
		data = {
			'name': 'John',
			'age': '40',
			'location': 'Houston',
			'bio': 'Lorem ipsum dolor sit amet'
		}
		response = self.client.post(url, data)
		john_profile = Profile.objects.get(location='Houston')
		self.assertEquals(john_profile.name, 'John')
		
	def test_profile_invalid_post(self):
		url = reverse('profile')
		response = self.client.post(url, {})
		self.assertEquals(response.status_code, 200)
		
	def test_contains_form(self):
		url = reverse('profile')
		response = self.client.get(url)
		form = response.context.get('form')
		self.assertIsInstance(form, ProfileUpdateForm)