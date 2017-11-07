from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import login, registration

urlpatterns = [
#    url(r'^login$', login),
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login_view'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login_view'}, name='logout'),
    url(r'^registration$', registration),
]
