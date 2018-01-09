from django.conf.urls import url

from .views import createPhotoseries, upload_done, upload_photos
from .forms import PhotoSeriesForm
urlpatterns = [

   
    url(r'^add/$', createPhotoseries.as_view(), name='upload'),
    url(r'^adds/$', upload_photos, name='uploads'),
    url(r'^adds_done/', upload_done, name='upload_done'),
]