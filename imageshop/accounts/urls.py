from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name' : 'accounts/login.html'}),
    url(r'^logout/$', login, {'template_name' : 'accounts/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile')


]