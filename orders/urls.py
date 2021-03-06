from django.conf.urls import url
from orders.views import viewMyOrders, viewOrder, viewMyOpenOrders, markOpenOrderAsPaid

urlpatterns = [
    url(r'^my/$', viewMyOrders.as_view(), name='myOrders'),
    url(r'^view/(?P<pk>[0-9]+)/$', viewOrder.as_view(), name='viewOrder'),
    url(r'^open/$', viewMyOpenOrders.as_view(), name='myOpenOrders'),
    url(r'^pay/(?P<pk>[0-9]+)/$', markOpenOrderAsPaid.as_view(), name='payOrder')
]