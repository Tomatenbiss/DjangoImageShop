from django.views.generic import ListView
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.core.exceptions import PermissionDenied, SuspiciousOperation

from orders.models import Order
from dynamicLink.models import Download
from imageshop import settings

import datetime
import random

# Create your views here.

class viewMyOrders(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_list.html'

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super(viewMyOrders, self).get_context_data(**kwargs)
        if self.request.user.groups.filter(name='photographer').exists():
             context['orders_as_seller'] = Order.objects.filter(seller=self.request.user)
        return context


class viewOrder(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/order_detailView.html'

    def get_context_data(self, **kwargs):
        context = super(viewOrder, self).get_context_data(**kwargs)
        if (self.request.user != context['object'].seller and self.request.user != context['object'].buyer):
            raise PermissionDenied
        return context


class viewMyOpenOrders(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_list.html'

    def get_queryset(self):
        return Order.objects.filter(seller=self.request.user, paid=False)
    
    def get_context_data(self, **kwargs):
        context = super(viewMyOpenOrders, self).get_context_data(**kwargs)
        if not self.request.user.groups.filter(name='photographer').exists():
             raise PermissionDenied
        return context

class markOpenOrderAsPaid(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'viewOrder'

    def get_redirect_url(self, *args, **kwargs):
        order = Order.objects.get(id=kwargs['pk'])
        if order.seller != self.request.user:
            raise PermissionDenied
        if order.paid:
            raise SuspiciousOperation("Order was already paid.")
        order.paid = True;
        order.paidDate = datetime.datetime.now();
        order.save();
        # Set download links
        for photo in order.photos.all():
            download = Download()
            download.slug = "slug_" + str(random.random())
            download.file_path = photo.image.name
            download.timeout_hours = 24
            download.max_clicks = 0
            download.save()
            order.downloads.add(download)
        order.save()
        download_link_string = ''
        for download_link in order.get_download_links():
            download_link_string += '<a href="' + str(download_link) + '">' + str(download_link) + '</a>\n'
        send_mail(
                'Order marked as payed',
                'Your order was marked as payed. Below are the download links for the photos:\n' + download_link_string,
                settings.EMAIL_HOST_USER,
                [order.buyer.email],
                fail_silently=True,
                auth_user=settings.EMAIL_HOST_USER,
                auth_password=settings.EMAIL_HOST_PASSWORD
        )
        return super(markOpenOrderAsPaid, self).get_redirect_url(*args, **kwargs)
