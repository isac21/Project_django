# Django_hello/urls.py

from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'Django_hello.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^admin/', include(admin.site.urls)),
]
