from django.conf.urls import url, include

from carts.views import add, clear, remove, show, add_series, remove_series

urlpatterns = [
    url(r'^add/$', add, name='add'),
    url(r'^add_series/$', add_series, name='add_series'),
    url(r'^clear/$', clear, name='clear'),
    url(r'^remove/$', remove, name='remove'),
    url(r'^remove_series/$', remove_series, name='remove_series'),
    url(r'^show/$', show, name='show'),
]
