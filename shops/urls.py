from django.conf.urls import url

from shops.views import viewAllPhotos

urlpatterns = [

    url(r'^(?P<username>.+)$', viewAllPhotos.as_view(), name='viewAllInShop')
]
