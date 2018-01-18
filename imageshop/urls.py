"""imageshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from accounts import urls as accounts_urls
from photos import urls as photos_urls
from photoseries import urls as photoseries_urls
from carts import urls as carts_urls
from shops import urls as shops_urls
from shops.views import viewAllShops
from search import urls as search_urls
from dynamicLink import presettings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', viewAllShops.as_view(), name='viewAllShops'),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^photos/', include(photos_urls)),
    url(r'^photoseries/', include(photoseries_urls)),
    url(r'^carts/', include(carts_urls, namespace='carts')),
    url(r'^shops/', include(shops_urls)),
    url(r'^search/', include(search_urls)),
    # for django-dynamic-link. By default it catch url/serve/some-dynamic-link/
    url(r'^w+/%s/' % presettings.DYNAMIC_LINK_URL_BASE_COMPONENT, include('dynamicLink.urls')),
    url(r'^lg/%s/' % presettings.DYNAMIC_LINK_URL_BASE_COMPONENT, include('dynamicLink.urls')),
    url(r'^de/%s/' % presettings.DYNAMIC_LINK_URL_BASE_COMPONENT, include('dynamicLink.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
