# main/urls

from django.conf.urls import include, url, patterns
from django.contrib import admin

from django.conf import settings

from .views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
]
