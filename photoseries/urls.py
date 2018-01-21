from django.conf.urls import url

from .views import  (createPhotoseries, 
                    upload_done, 
                    upload_photos,  
                    viewPhotoseries, 
                    viewOwnPhotoseries, 
                    updatePhotoseries,
                    deletePhotoseries)

from .forms import PhotoSeriesForm
urlpatterns = [
    # view photoseries
   url(r'^view/(?P<pk>[0-9]+)/$', viewPhotoseries.as_view(), name='view_series'),
   url(r'^thumb/(?P<pk>[0-9]+)/$', viewPhotoseries.as_view(), name='view_series'),

    # upload from existing images
    url(r'^add/$', createPhotoseries.as_view(), name='upload_series'),
    # uplaod new images into series
    url(r'^adds/$', upload_photos, name='uploads_series'),
    # success url for the upload -- deprecated soon
    url(r'^adds_done/', upload_done, name='upload_done'),
    url(r'^owned/$', viewOwnPhotoseries.as_view(), name='viewOwn_series'),
    url(r'^edit/(?P<pk>[0-9]+)/$', updatePhotoseries.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', deletePhotoseries.as_view(), name='delete'),


]
