from django.shortcuts import render, redirect, render_to_response
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

def upload_photos(request):
    if request.method == "POST":
        files = request.FILES.getlist('images')
        describtion = request.POST['describtion']
        title = request.POST['title']
        for number, a_file in enumerate(files):
            instance = Photo(image=a_file, owner = request.user)
            instance.save()
        return redirect('upload_done')

    return render(request, 'photos/upload.html')


def upload_done(request):
    return render_to_response('photos/upload_done.html')