
from django.views.generic import UpdateView, ListView,\
    DetailView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Robot


class HomePage(ListView):
    template_name = 'bots/index.html'
    context_object_name = 'robot_report'

    def get_queryset(self):
        return Robot.objects.order_by('name')


class RobotDetail(DetailView):
    model = Robot
    template_name = 'bots/detail.html'


class RobotUpdate(UpdateView):
    model = Robot
    fields = ['name', 'speed', 'battery_life', 'strength']
    template_name = 'bots/update.html'
    success_url = reverse_lazy('index')


class DeleteRobot(DeleteView):
    model = Robot
    success_url = reverse_lazy('index')
    template_name = 'bots/delete.html'


class CreateRobot(CreateView):
    model = Robot
    fields = ['name', 'speed', 'battery_life', 'strength']
    success_url = reverse_lazy('index')
    template_name = 'bots/robot_form.html'
