# photos/urls.py

from django.conf.urls import include, url, patterns
from django.contrib import admin
#from django.conf import settings
#from django.conf.urls.static import static

from photos.views import hello, detail



urlpatterns = [
    url(r'^$', hello),
    url(r'^(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r'^admin/', admin.site.urls),
]

#urlpatterns += static('/upload_files/', document_root=settings.MEDIA_ROOT)
