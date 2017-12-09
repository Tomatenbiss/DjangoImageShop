from django.conf.urls import url

from photos.views import viewPhoto, createPhoto, updatePhoto, deletePhoto, viewAllPhotos, viewOwnPhotos, categoryView

urlpatterns = [

    url(r'^view/(?P<pk>[0-9]+)/$', viewPhoto.as_view(), name='view'),
    url(r'^view/$', viewAllPhotos.as_view(), name='viewAll'),
    url(r'^add/$', createPhoto.as_view(), name='upload'),
    url(r'^edit/(?P<pk>[0-9]+)/$', updatePhoto.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', deletePhoto.as_view(), name='delete'),
    url(r'^owned/$', viewOwnPhotos.as_view(), name='viewOwn'),
    url(r'^categories/add/$', categoryView.as_view(), name='category_add'),
    # temporary view for categories
    url(r'^categories/$', categoryView.as_view(), name='categories')
]