# Django_hello/urls.py

from django.conf.urls import include, url, patterns
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views


urlpatterns = [

    url(r'^$', include('main.urls')),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^photos/',include('photos.urls', namespace="photos")),
    url(r'^admin/', include(admin.site.urls)),

    #log-in
    url(r'^accounts/login/',
        auth_views.login,
        name='login',
        kwargs={'template_name': 'login.html'}),

    #log-out
    url(r'^accounts/logout/',
        auth_views.logout,
        name='logout',
        kwargs={'next_page': settings.LOGIN_URL}),
]

urlpatterns += static('/upload_files/', document_root=settings.MEDIA_ROOT)
