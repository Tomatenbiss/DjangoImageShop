from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from accounts.views import registration, profile

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login_view'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login_view'}, name='logout'),
    url(r'^registration$', registration, name='registration'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'accounts/registration/password_reset_form.html'}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'accounts/registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'template_name': 'accounts/registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name': 'accounts/registration/password_reset_complete.html'}, name='password_reset_complete'),
]
