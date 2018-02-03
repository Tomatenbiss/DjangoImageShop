from django.views.generic import View, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from .models import Photo, PhotoCategory
from orders.models import Order

class OwnerRequiredView(object):
    
    def get_context_data(self, **kwargs):
        context = super(OwnerRequiredView, self).get_context_data(**kwargs)
        if context['object'].owner != self.request.user:
            raise PermissionDenied
        return context


class categoryView(CreateView):
    model = PhotoCategory
    fields = ['name']
    template_name = 'photos/categories.html'

    def get_context_data(self, **kwargs):
        context = super(categoryView, self).get_context_data(**kwargs)
        context['categories'] = PhotoCategory.objects.filter();
        return context


class deleteCategory(LoginRequiredMixin, DeleteView):
    model = PhotoCategory
    success_url = '/photos/categories/'


class viewPhoto(DetailView):
    model = Photo
    template_name = 'photos/photo_detailView.html'

    def get_context_data(self, **kwargs):
        context = super(viewPhoto, self).get_context_data(**kwargs)
        if context['object'].order_copy:
            context['order'] = Order.objects.get(photos__in=[context['object']])
            if (self.request.user != context['order'].seller and self.request.user != context['order'].buyer):
                raise PermissionDenied
        return context


class viewAllPhotos(ListView):
    model = Photo
    template_name = 'photos/photo_list.html'

    def get_queryset(self):
        '''Only retrieve photos who are visible'''
        return Photo.objects.filter(public=True, order_copy=False)


class createPhoto(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['title', 'description', 'image', 'price', 'public', 'categories']
    template_name = 'photos/photo_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.created = timezone.now()
        form.instance.last_modified = timezone.now()
        return super(createPhoto, self).form_valid(form)


class updatePhoto(LoginRequiredMixin, OwnerRequiredView, UpdateView):
    model = Photo
    fields = ['title', 'description', 'price', 'public', 'categories']
    template_name = 'photos/photo_form.html'

    def get_context_data(self, **kwargs):
        context = super(updatePhoto, self).get_context_data(**kwargs)
        if context['object'].order_copy:
            raise PermissionDenied
        return context

    def form_valid(self, form):
        form.instance.last_modified = timezone.now()
        return super(updatePhoto, self).form_valid(form)


class deletePhoto(LoginRequiredMixin, OwnerRequiredView, DeleteView):
    model = Photo
    success_url = '/photos/view/'

    def get_context_data(self, **kwargs):
        context = super(deletePhoto, self).get_context_data(**kwargs)
        if context['object'].order_copy:
            raise PermissionDenied
        return context


class viewOwnPhotos(LoginRequiredMixin, ListView):
    model = Photo

    def get_queryset(self):
        '''Only show photos of the current User'''
        return Photo.objects.filter(owner=self.request.user, order_copy=False)
