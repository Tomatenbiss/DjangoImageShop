from django.conf.urls import url

from photo.views import createPhoto, updatePhoto

urlpatterns = [

    url(r'^upload$', createPhoto.as_view(), name='upload'),
    url(r'^update/<pk>$', updatePhoto.as_view(), name='update'),
]