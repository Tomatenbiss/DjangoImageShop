from django.conf.urls import url, include

from shoppingcart.views import add, remove, show

urlpatterns = [
    url(r'^add/$', add, name='add'),
    url(r'^remove/$', remove, name='remove'),
    url(r'^show/$', show, name='show'),
]
