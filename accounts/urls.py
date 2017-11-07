from django.conf.urls import url

from accounts.views import login, registration, profile

urlpatterns = [
    url(r'^login$', login),
    url(r'^registration$', registration),
    url(r'^profile$', profile),
]