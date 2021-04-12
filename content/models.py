from django.db import models
from django.contrib.auth.models import User

class Chapter(models.Model):
	index = models.IntegerField(default=0, unique=True)
	title = models.CharField(max_length=60, unique=True)
	tag_line = models.CharField(max_length=500)
	video_embed = models.CharField(max_length=300)
	transcript = models.CharField(max_length=1000, blank=True)
	
	def __str__(self):
		return self.title
	
class Author(models.Model):
	first_name: models.CharField(max_length=30)
	last_name: models.CharField(max_length=30)
	
class Keyword(models.Model):
	keyword = models.CharField(max_length=30)
	
class Article(models.Model):
	title = models.CharField(max_length=60, unique=True)
	authors = models.ManyToManyField(Author)
	embed = models.CharField(max_length=100)
	summary = models.TextField(max_length=500)
	keywords = models.ManyToManyField(Keyword)
	
class Video(models.Model):
	title = models.CharField(max_length=60, unique=True)
	authors = models.CharField(max_length=200)
	embed = models.CharField(max_length=300)
	summary = models.TextField(max_length=500)
	keywords = models.ManyToManyField(Keyword)

class Review(models.Model):
	chapter = models.ForeignKey(Chapter, related_name='review', on_delete=models.DO_NOTHING)
	first_p = models.TextField(max_length=500)
	first_img = models.CharField(max_length=300)
	second_p = models.TextField(max_length=500)
	second_img = models.CharField(max_length=300)
	third_p = models.TextField(max_length=500)
	third_img = models.CharField(max_length=300)

	def __str__(self):
		return '{} Review'.format(self.chapter.title)

DEFAULT_CURRENT_ID = 1
DEFAULT_PREVIOUS_ID = 0
DEFAULT_NEXT_ID = 2

class Progress(models.Model):
	user = models.OneToOneField(User, related_name='progress', on_delete=models.CASCADE)
	current_chapter = models.ForeignKey(Chapter, default=DEFAULT_CURRENT_ID, related_name='current', on_delete=models.DO_NOTHING)
	