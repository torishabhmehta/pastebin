from django import forms
from django.forms import ModelForm
from snippets.models import Comment
class SnippetForm(forms.Form):
	title = forms.CharField(label='Title', max_length=30)
	content = forms.CharField(label='Content', widget=forms.Textarea)

class Commentform(forms.ModelForm):
	class Meta:
		model=Comment
		fields=['content']
	
