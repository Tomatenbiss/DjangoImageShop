from django.conf.urls import url

from photo.views import createPhoto, updatePhoto

urlpatterns = [

    url(r'^add$', createPhoto.as_view(), name='upload'),
    url(r'^edit/<pk>$', updatePhoto.as_view(), name='update'),
]