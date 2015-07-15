from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^bots/(?P<robot_id>[0-9]+)/update/$', views.RobotUpdate.as_view(), name='update'),
    url(r'^bots/add_robot/$', views.add_robot, name='add_robot'),
    #url(r'^(?P< post_url>\w+)/$', views.post, name='post'),

    ]

    #url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
   # url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
#)
