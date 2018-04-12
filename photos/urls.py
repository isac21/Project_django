# photos/urls.py

from django.conf.urls import include, url, patterns
from django.contrib import admin


from .views import hello, detail, create



urlpatterns = [
    url(r'^$', hello),
    url(r'^(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r'^upload/$', create, name='create'),

    url(r'^admin/', admin.site.urls),
]
