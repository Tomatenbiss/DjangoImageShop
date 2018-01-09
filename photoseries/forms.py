from django import forms
from .models import Photoseries
from multiupload.fields import MultiFileField

class PhotoSeriesForm(forms.ModelForm):
    
    class Meta:
        model = Photoseries
        fields = (
            'images', 
            'describtion', 
            'title',
        )
    images = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

    def save(self, commit=True):
        PhotoSeries.images      = self.cleaned_data['images']
        PhotoSeries.description = self.cleaned_data['description']
        PhotoSeries.tags        = self.cleaned_data['tags']
        PhotoSeries.title       = self.cleaned_data['title']
        return PhotoSeries