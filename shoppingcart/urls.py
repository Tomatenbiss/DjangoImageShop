from django.conf.urls import url, include

from shoppingcart.views import registration, show

urlpatterns = [
    url(r'^registration$', registration, name='registration'),
    url(r'^show/$', show, name='show'),
]
