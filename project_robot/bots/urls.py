from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<robot_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'(?P<robot_id>[0-9]+)/edit', views.edit, name='edit')
    ]
