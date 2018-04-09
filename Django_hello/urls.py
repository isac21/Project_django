# Django_hello/urls.py

from django.conf.urls import include, url, patterns
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^photos/',include('photos.urls', namespace="photos")),
    url(r'^admin/', include(admin.site.urls)),
]
    #url(r'^photos/(?P<pk>[0-9]+/$',
#        detail, name='detail'),

urlpatterns += static('/upload_files/', document_root=settings.MEDIA_ROOT)
