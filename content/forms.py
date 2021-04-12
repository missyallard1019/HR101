from django import forms
from django.forms import ModelForm
from .models import Progress
		
class ProgressUpdateForm(forms.ModelForm):

	class Meta:
		model = Progress
		fields = ('current_chapter',)