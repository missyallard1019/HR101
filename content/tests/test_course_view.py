from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from ..views import home, education, course
from ..models import Chapter, Review, Progress
from ..forms import ProgressUpdateForm

class LoginRequiredCourseTests(TestCase):
	def setUp(self):
		chapter = Chapter.objects.create(title="Test Chapter", tag_line="This is a test")
		review = Review.objects.create(chapter=chapter, first_p="Test paragraph", first_img="test.img", second_p="Test paragraph", second_img="test.img", third_p="Test paragraph", third_img="test.img")
		self.url = reverse('course', kwargs={'index': 2})
		self.response = self.client.get(self.url)
		
	def test_redirection(self):
		login_url = reverse('login')
		self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))

class CourseTests(TestCase):
	def setUp(self):
		user = User.objects.create_user(username='john', email='john@doe.com', password='123')
		self.client.login(username='john', password='123')
		chapter2 = Chapter.objects.create(index=1, title="Test Chapter 2", tag_line="This is a test 2")
		review = Review.objects.create(chapter=chapter2, first_p="Test paragraph", first_img="test.img", second_p="Test paragraph", second_img="test.img", third_p="Test paragraph", third_img="test.img")
		progress = Progress.objects.create(pk=1, user=user, current_chapter=chapter2)
		index = chapter2.index
		self.url = reverse('course', kwargs={'index': index})
		self.response = self.client.get(self.url)
		
	def test_course_view_status_code(self):
		self.assertEquals(self.response.status_code, 200)
		
	def test_course_url_resolves_course_view(self):
		view = resolve('/course/1/')
		self.assertEquals(view.func, course)