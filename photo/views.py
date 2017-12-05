from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from .models import Photo, PhotoCategory
from django.http.response import JsonResponse

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                # BAD - this works only for categories
                'name': form.instance.name,
            }
            return JsonResponse(data, status=200)
        else:
            return response

class categoryView(AjaxableResponseMixin, CreateView):
    model = PhotoCategory
    fields = ['name']
    template_name = 'photo/categories.html'

    def get_context_data(self, **kwargs):
        context = super(categoryView, self).get_context_data(**kwargs)
        context['categories'] = PhotoCategory.objects.filter();
        return context


class viewPhoto(DetailView):
    model = Photo
    template_name = 'photo/photo_detailView.html'


class viewAllPhotos(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'

    def get_queryset(self):
        '''Only retrieve photos who are visible'''
        return Photo.objects.filter(public=True)


class createPhoto(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['title', 'description', 'image', 'price', 'public']
    template_name = 'photo/photo_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.created = timezone.now()
        form.instance.last_modified = timezone.now()
        return super(createPhoto, self).form_valid(form)


class updatePhoto(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['title', 'description', 'price', 'public']
    template_name = 'photo/photo_form.html'

    def form_valid(self, form):
        if form.instance.owner != self.request.user :
            raise PermissionDenied
        form.instance.last_modified = timezone.now()
        return super(updatePhoto, self).form_valid(form)
