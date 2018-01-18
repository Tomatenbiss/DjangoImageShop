from django.shortcuts import render, redirect, render_to_response
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Photoseries
from photos.models import Photo
from django.utils import timezone

# form for photoseries
class createPhotoseries(LoginRequiredMixin, CreateView):
    model = Photoseries
    # fields that can be edited
    fields = ['title', 'description', 'images', 'price']
    template_name = 'photoseries/photoseries_form.html'
    
    # set owner based on session and add timestamps
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.created = timezone.now()
        form.instance.last_modified = timezone.now()
        return super(createPhotoseries, self).form_valid(form)

    # get images from photographer and display them for selection
    def get_form(self, *args, **kwargs):
        form = super(createPhotoseries, self).get_form(*args, **kwargs)
        #form.fields['images'].queryset = self.request.user.a_set.all()
        form.fields['images'].queryset = Photo.objects.filter(owner=self.request.user)
        return form

def upload_photos(request):
    if request.method == "POST":
        # get fields from page and build object
        files = request.FILES.getlist('images')
        description = request.POST['description']
        title = request.POST['title']
        price = 2.0
        s_instance = Photoseries(title = title , description = description, owner=request.user ,price = price)
        # save series before adding images
        s_instance.save()
        # iterate over files
        for count,a_file in enumerate(files):
            # create & save Image for every file
            p_instance = Photo(image=a_file, owner=request.user, public = False)
            p_instance.save()
            # add image to series
            s_instance.images.add(p_instance)
        # save modified series
        s_instance.save()
        return redirect('upload_done')

    return render(request, 'photoseries/upload.html')


def upload_done(request):
    return render_to_response('photoseries/upload_done.html')

class viewPhotoseries(DetailView):
    model = Photoseries
    template_name = 'photoseries/photoseries_detailView.html'

class viewOwnPhotoseries(LoginRequiredMixin, ListView):
    model = Photoseries

    def get_queryset(self):
        '''Only show photos of the current User'''
        return Photoseries.objects.filter(owner=self.request.user)

