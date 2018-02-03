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
from orders.models                  import Order
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
        pric = request.POST['price']
        pub = request.POST.get('public', False)
        if (pub == 'on'):
            pub = False
        s_instance = Photoseries(title = title , description = description, owner=request.user ,price = pric, public = pub)
        # save series before adding images
        s_instance.save(False)
        # iterate over files
        for count,a_file in enumerate(files):
            # create & save Image for every file
            p_instance = Photo(image=a_file, owner=request.user, public = pub)
            p_instance.save(True)
            # add image to series
            s_instance.images.add(p_instance)
        # save modified series
        s_instance.save()
        return redirect('/photoseries/list/')

    return render(request, 'photoseries/upload.html')


def upload_done(request):
    return render_to_response('photoseries/upload_done.html')

class viewPhotoseries(DetailView):
    model = Photoseries
    template_name = 'photoseries/photoseries_detailView.html'

    def get_context_data(self, **kwargs):
        context = super(viewPhotoseries, self).get_context_data(**kwargs)
        if context['object'].order_copy:
            context['order'] = Order.objects.get(photoseries__in=[context['object']])
            if (self.request.user != context['order'].seller and self.request.user != context['order'].buyer):
                raise PermissionDenied
        return context

class viewOwnPhotoseries(LoginRequiredMixin, ListView):
    model = Photoseries

    def get_queryset(self):
        '''Only show photos of the current User'''
        return Photoseries.objects.filter(owner=self.request.user, order_copy=False)

class listPhotoseries(LoginRequiredMixin, ListView):
    model = Photoseries
    template_name = 'photoseries/photoseries_list.html'

    def get_queryset(self):
        return Photoseries.objects.filter(order_copy=False)

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