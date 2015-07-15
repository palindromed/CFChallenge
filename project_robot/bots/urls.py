from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(),
        name='detail'),
    url(r'^robot_update_form/(?P<pk>[0-9]+)/$', views.RobotUpdate.as_view(),
        name='update'),
    url(r'^robot_form/$', views.CreateRobot.as_view(), name='robot_form'),
    url(r'^robot_confirm_delete/(?P<pk>[0-9]+)/$', views.DeleteRobot.as_view(),
        name='delete')

    ]
