from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from accounts.views import registration, profile

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login_view'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login_view'}, name='logout'),
    url(r'^registration$', registration, name='registration'),
    url(r'^profile$', profile, name='profile'),
]
