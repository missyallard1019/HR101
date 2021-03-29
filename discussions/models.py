from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.db.models.signals import post_save
from django.dispatch import receiver

class Board(models.Model):
	name = models.CharField(max_length=30, unique=True)
	description = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
	
	def get_posts_count(self):
		return Post.objects.filter(topic__board=self).count()
	
	def get_last_post(self):
		return Post.objects.filter(topic__board=self).order_by('-created_at').first()

	
class Topic(models.Model):
	subject = models.CharField(max_length=140)
	last_updated = models.DateTimeField(auto_now_add=True)
	board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
	starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
	views = models.PositiveIntegerField(default=0)
	
	def __str__(self):
		return self.subject
	
	
class Post(models.Model):
	message = models.TextField(max_length=500)
	topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
	updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
	
	def __str__(self):
		truncated_message = Truncator(self.message)
		return truncated_message.chars(30)
	
class Profile(models.Model):
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	name = models.CharField(max_length=30, blank=True)
	age = models.IntegerField(null=True, blank=True)
	user_type = models.CharField(max_length=30, blank=True)
	location = models.CharField(max_length=30, blank=True)
	bio = models.TextField(max_length=500, blank=True)
	
	def __str__(self):
		return self.user.username
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
		
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
	
class Direct(models.Model):
	message = models.TextField(max_length=500)
	subject = models.CharField(max_length=140)
	sent_at = models.DateTimeField(auto_now_add=True)
	sent_by = models.ForeignKey(User, related_name='outbox', on_delete=models.DO_NOTHING)
	sent_to = models.ForeignKey(User, related_name='inbox', on_delete=models.DO_NOTHING)
	
	def __str__(self):
		truncated_message = Truncator(self.message)
		return truncated_message.chars(30)
	
class Group(models.Model):
	name = models.CharField(max_length=30, unique=True)
	description = models.CharField(max_length=100)
	#members - TODO
	
	def __str__(self):
		return self.name