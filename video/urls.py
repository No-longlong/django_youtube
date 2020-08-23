from django.conf.urls import url, include
from . import views
#from django.core import urlresolvers

app_name = 'video'

urlpatterns = [
    url('$', views.video_list, name='list')
]