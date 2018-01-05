from django.conf.urls import url

from .views import createPhotoseries

urlpatterns = [

   
    url(r'^add/$', createPhotoseries.as_view(), name='upload'),
]