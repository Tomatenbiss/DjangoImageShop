from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from .models import Photo


class viewPhoto(DetailView):
    model = Photo
    template_name = 'photo/photo_detailView.html'


class viewAllPhotos(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'

    def get_context_data(self, **kwargs):
        context = super(viewAllPhotos, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class createPhoto(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['title', 'description', 'image']
    template_name = 'photo/photo_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.created = timezone.now()
        form.instance.last_modified = timezone.now()
        return super(createPhoto, self).form_valid(form)


class updatePhoto(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['title', 'description']
    template_name = 'photo/photo_form.html'

    def form_valid(self, form):
        if form.instance.owner != self.request.user :
            raise PermissionDenied
        form.instance.last_modified = timezone.now()
        return super(updatePhoto, self).form_valid(form)
