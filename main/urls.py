# main/urls

from django.conf.urls import include, url, patterns
from django.contrib import admin

from django.conf import settings

from .views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls, name='index'),
]
