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

from accounts.views import start_view
from accounts import urls as accounts_urls
from photos import urls as photos_urls
from carts import urls as carts_urls
from imagefit import urls as imagefit_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', start_view, name='start_view'),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^photos/', include(photos_urls)),
    url(r'^carts/', include(carts_urls, namespace='carts')),
    url(r'^imagefit/', include(imagefit_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
