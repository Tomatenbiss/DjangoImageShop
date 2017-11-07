from django.conf.urls import url

from accounts.views import login, registration

urlpatterns = [
    url(r'^login$', login),
    url(r'^registration$', registration),
]