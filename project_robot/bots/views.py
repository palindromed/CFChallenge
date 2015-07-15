
from django.views.generic import UpdateView, ListView,\
    DetailView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext


from .models import Robot
#from .forms import MakeRobotForm, UpdateForm


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
    fields = ['name', 'speed', 'battery_life', 'strength']
    template_name = 'bots/update.html'

    #def get_object(self, queryset=None):
     #   pk = self.kwargs.get(self.pk_url_kwarg)
      #  slug = self.kwargs.get(self.slug_url_kwarg)
       # if pk is not None:
#            queryset = queryset.filter(pk=pk)

 #   def form_valid(self, form):
  #      clean = form.cleaned_data
   #     context = {}
    #    self.object = context.save(clean)
     #   return super(UpdateForm, self).form_valid(form)


class DeleteRobot(DeleteView):
    model = Robot
    success_url = reverse_lazy('index')
    template_name = 'bots/delete.html'


class CreateRobot(CreateView):
    model = Robot
    fields = ['name', 'speed', 'battery_life', 'strength']
    success_url = reverse_lazy('index')
    template_name = 'bots/robot_form.html'
