from django import forms
from .models import PhotoCategory, Photo

class AddCategory(forms.ModelForm):
	categories = forms.MultipleChoiceField(
	    choices=PhotoCategory,
	    widget=forms.CheckboxSelectMultiple(),
	    required=False
	)
