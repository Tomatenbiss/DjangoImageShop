from django.shortcuts               import (render, 
                                            redirect, 
                                            render_to_response)
from django.views.generic           import ListView
from django.views.generic.edit      import (CreateView, 
                                            UpdateView, 
                                            DeleteView)
from django.views.generic.detail    import DetailView
from django.contrib.auth.mixins     import LoginRequiredMixin
from .models                        import Photoseries
from photos.models                  import Photo
from django.utils                   import timezone
from django.core.exceptions         import PermissionDenied


class OwnerRequiredView(object):
    
    def get_context_data(self, **kwargs):
        context = super(OwnerRequiredView, self).get_context_data(**kwargs)
        if context['object'].owner != self.request.user:
            raise PermissionDenied
        return context

# form for photoseries
class createPhotoseries(LoginRequiredMixin, CreateView):
    model = Photoseries
    # fields that can be edited
    fields = ['title', 
                'description', 
                'images', 
                'price', 
                'public']
    template_name = 'photoseries/photoseries_form.html'
    # set owner based on session and add timestamps
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.created = timezone.now()
        form.save()
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
        pub = False
        price = 2.0
        s_instance = Photoseries(title = title , description = description, owner=request.user ,price = price, public = pub)
        # save series before adding images
        s_instance.save()
        # iterate over files
        for count,a_file in enumerate(files):
            # create & save Image for every file
            p_instance = Photo(image=a_file, owner=request.user, public = pub)
            p_instance.save()
            # add image to series
            s_instance.images.add(p_instance)
        # save modified series
        s_instance.save()
        return redirect(viewPhotoseries)

    return render(request, 'photoseries/upload.html')


def upload_done(request):
    return render_to_response('photoseries/upload_done.html')

class viewPhotoseries(DetailView):
    model = Photoseries
    template_name = 'photoseries/photoseries_thumbnail.html'

class viewOwnPhotoseries(LoginRequiredMixin, ListView):
    model = Photoseries

    def get_queryset(self):
        '''Only show photos of the current User'''
        return Photoseries.objects.filter(owner=self.request.user)

class updatePhotoseries(LoginRequiredMixin, UpdateView):
    model = Photoseries
    fields = ['title', 
                'description', 
                'price', 
                'public', 
                ]
    template_name = 'photoseries/photoseries_form.html'

    def form_valid(self, form):
        form.instance.last_modified = timezone.now()
        return super(updatePhotoseries, self).form_valid(form)

class deletePhotoseries(LoginRequiredMixin, OwnerRequiredView, DeleteView):
    model = Photoseries
    success_url = '/photoseries/list/'