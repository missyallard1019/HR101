from django import forms
from .models import Topic, Post, Profile

class NewTopicForm(forms.ModelForm):
	message = forms.CharField(widget=forms.Textarea(), max_length=4000)
	
	class Meta:
		model = Topic
		fields = ['subject', 'message']
		
class PostForm(forms.ModelForm):
	message = forms.CharField(widget=forms.Textarea(), max_length=4000, label='Post a reply:')
	
	class Meta:
		model = Post
		fields = ['message']
		
class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ('name', 'age', 'location', 'bio')
		
	def clean(self):
		return self.cleaned_data