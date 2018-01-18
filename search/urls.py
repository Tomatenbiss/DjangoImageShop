from django.conf.urls import url

from search.views import searchResultView

urlpatterns = [
    url(r'^$', searchResultView.as_view(), name="search"),
]