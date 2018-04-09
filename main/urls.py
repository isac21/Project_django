# main/urls

from django.conf.urls import include, url, patterns
from django.contrib import admin

from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
