from django.conf.urls import url

from photo.views import viewPhoto, createPhoto, updatePhoto, viewAllPhotos

urlpatterns = [

    url(r'^view/(?P<pk>[0-9]+)/$', viewPhoto.as_view(), name='view'),
    url(r'^view/$', viewAllPhotos.as_view(), name='viewAll'),
    url(r'^add/$', createPhoto.as_view(), name='upload'),
    url(r'^edit/(?P<pk>[0-9]+)/$', updatePhoto.as_view(), name='update'),
]