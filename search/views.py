from django.views.generic import TemplateView
from photos.models import Photo, PhotoCategory
from photoseries.models import Photoseries

# Create your views here.

class searchResultView(TemplateView):
    template_name = 'search/search_result.html'

    def get_context_data(self):
        context = {}
        keyword = self.request.GET['keyword']
        context['keyword'] = keyword
        # Search for photos
        context['photos_found_by_title'] = Photo.objects.filter(title__contains=keyword)
        context['photos_found_by_description'] = Photo.objects.filter(description__contains=keyword)
        context['categories'] = PhotoCategory.objects.filter(name__contains=keyword)
        context['photos_found_by_category'] = Photo.objects.filter(categories__in=context['categories'])
        # Search for photoseries
        context['photoseries_found_by_title'] = Photoseries.objects.filter(title__contains=keyword)
        context['photoseries_found_by_description'] = Photoseries.objects.filter(description__contains=keyword)
        return context;
