
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Photo

class create_photo(CreateView):
    model   = Photo
    fields  = [ 'titel',
                'description',
                'public'
    ]

class update_photo(UpdateView):
    model = Photo
    fields = ['name']
