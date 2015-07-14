from django.shortcuts import render, get_object_or_404
#from django.views.generic import ListView, DetailView, UpdateView
#from django.core.urlresolvers import reverse
from django.http import Http404

from .models import Robot


def index(request):
    robot_report = Robot.objects.order_by('name')
    print(robot_report)
    context = {'robot_report': robot_report}
    return render(request, 'bots/index.html', context)


def detail(request, robot_id):
    try:
        robot = get_object_or_404(Robot, pk=robot_id)
    except Robot.DoesNotExist:
        raise Http404('That robot does not exist')
    return render(request, 'bots/detail.html', {'robot': robot})


