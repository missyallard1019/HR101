from django.db import models

class Chapter(models.Model):
	index = models.IntegerField(default=0, unique=True)
	title = models.CharField(max_length=60, unique=True)
	tag_line = models.CharField(max_length=140)
	video_embed = models.CharField(max_length=100)
	transcript = models.TextField(max_length=1000)
	#ext_links = ????
	
#class Authors(models.Model) ???
#class Keywords ???
	
class Article(models.Model):
	title = models.CharField(max_length=60, unique=True)
	authors = models.CharField(max_length=140)
	embed = models.CharField(max_length=100)
	summary = models.TextField(max_length=500)
	#keywords = ???
	
class Video(models.Model):
	title = models.CharField(max_length=60, unique=True)
	authors = models.CharField(max_length=140)
	embed = models.CharField(max_length=100)
	summary = models.TextField(max_length=500)
	#keywords = ???

class Review(models.Model):
	chapter = models.ForeignKey(Chapter, related_name='review', on_delete=models.DO_NOTHING)
	first_p = models.TextField(max_length=500)
	first_img = models.CharField(max_length=100)
	second_p = models.TextField(max_length=500)
	second_img = models.CharField(max_length=100)
	third_p = models.TextField(max_length=500)
	third_img = models.CharField(max_length=100)
