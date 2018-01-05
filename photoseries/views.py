from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Photoseries
from photos.models import Photo
from django.utils import timezone

# Create your views here.
class createPhotoseries(LoginRequiredMixin, CreateView):
    model = Photoseries
    fields = ['title', 'describtion', 'images']
    template_name = 'photos/photo_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.created = timezone.now()
        form.instance.last_modified = timezone.now()
        return super(createPhotoseries, self).form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super(createPhotoseries, self).get_form(*args, **kwargs)
        #form.fields['images'].queryset = self.request.user.a_set.all()
        form.fields['images'].queryset = Photo.objects.filter(owner=self.request.user) 
        return form