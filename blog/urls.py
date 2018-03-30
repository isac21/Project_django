# blog/urls.py

from django.conf.urls import url, patterns
from blog import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'Django_hello.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='detail'),
]
