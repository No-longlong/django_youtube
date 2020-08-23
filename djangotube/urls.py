# djangotube/urls.py
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/', include('video.urls', namespace='video')),
]