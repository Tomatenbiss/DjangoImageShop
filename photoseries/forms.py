from django import forms
from .models import Photoseries

class PhotoSeriesForm(forms.ModelForm):
    
    class Meta:
        model = Photoseries
        fields = (
            'images', 
            'description', 
            'tags',
            'title',
        )
    images = forms.ImageField(label="Bild wählen")
    
    def save(self, commit=True):
        PhotoSeries.images      = self.cleaned_data['images']
        PhotoSeries.description = self.cleaned_data['description']
        PhotoSeries.tags        = self.cleaned_data['tags']
        PhotoSeries.title       = self.cleaned_data['title']
        return PhotoSeries
