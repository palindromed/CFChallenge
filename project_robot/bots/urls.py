from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='index'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.RobotDetail.as_view(),
        name='detail'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.RobotUpdate.as_view(),
        name='update'),
    url(r'^robot_form/$', views.CreateRobot.as_view(), name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.DeleteRobot.as_view(),
        name='delete')
    ]
