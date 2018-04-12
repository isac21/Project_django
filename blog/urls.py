# blog/urls.py

from django.conf.urls import url, patterns
from .views import index, title


urlpatterns = [

#    url(r'^$', index, name='index'),
    url(r'^$', title, name='title'),
]
