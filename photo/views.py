
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Photo


class createPhoto(CreateView):
    model = Photo
    fields = ['title', 'description', 'image']
    template_name = 'photo/photo_form.html'


class updatePhoto(UpdateView):
    model = Photo
    fields = ['name']
    template_name = 'photo/photo_form.html'
