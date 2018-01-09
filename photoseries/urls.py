from django.conf.urls import url

from .views import createPhotoseries, upload_done, upload_photos, viewPhotoseries
from .forms import PhotoSeriesForm
urlpatterns = [

   url(r'^view/(?P<pk>[0-9]+)/$', viewPhotoseries.as_view(), name='view'),
    url(r'^add/$', createPhotoseries.as_view(), name='upload'),
    url(r'^adds/$', upload_photos, name='uploads'),
    url(r'^adds_done/', upload_done, name='upload_done'),
]