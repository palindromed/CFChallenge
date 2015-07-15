from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.views.generic import UpdateView, ListView, DetailView
from django.template import RequestContext

from .models import Robot
from .forms import MakeRobotForm, UpdateForm


class IndexView(ListView):
    template_name = 'bots/index.html'
    context_object_name = 'robot_report'

    def get_queryset(self):
        return Robot.objects.order_by('name')


class DetailView(DetailView):
    model = Robot
    template_name = 'bots/detail.html'


class RobotUpdate(UpdateView):
    model = Robot
    form_class = UpdateForm
    fields = ['name', 'speed', 'battery_life', 'strength']
    template_name = 'update.html'
    success_url = IndexView

    def get_object(self):
        return get_object_or_404(Robot, pk='robot_id')

    #get object
    #def get_robot(self, queryset=None):
    #    return self.request.robot

    def form_valid(self, form):
        clean = form.cleaned_data
        context = {}
        self.object = context.save(clean)
        return super(RobotUpdate, self).form_valid(form)


def add_robot(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = MakeRobotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('bots/index.html/')
        else:
            print(form.errors)
    else:
        form = MakeRobotForm()
        return render_to_response('bots/add_robot.html', {'form': form}, context)
