from django.conf.urls import url, include

from carts.views import add, clear, remove, show, checkoutView

urlpatterns = [
    url(r'^add/$', add, name='add'),
    url(r'^clear/$', clear, name='clear'),
    url(r'^remove/$', remove, name='remove'),
    url(r'^show/$', show, name='show'),
    url(r'^checkout/$', checkoutView.as_view(), name="checkout"),
]
