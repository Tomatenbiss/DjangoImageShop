from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    
    class Meta:
        model = Photo
        fields = (
            'image', 
            'description', 
            'tags',
            'created',
            'last_modified',
            'title',
            'public',
        )

    
    def save(self, commit=True):
        Photo.image = self.cleaned_data['owner']
        Photo.description = self.cleaned_data['description']
        Photo.tags = self.cleaned_data['tags']
        Photo.title = self.cleaned_data['title']
        Photo.public = self.cleaned_data['public']
        return Photo
