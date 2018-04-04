# blog/urls.py

from django.conf.urls import url, patterns
from blog import views


urlpatterns = [

    url(r'^$', views.index, name='detail'),
]
