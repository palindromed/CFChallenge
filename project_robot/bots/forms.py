from django import forms
from bots.models import Robot


class MakeRobotForm(forms.ModelForm):
    class Meta:
        model = Robot
        fields = ['name', 'speed', 'battery_life', 'strength']


#class UpdateForm(forms.ModelForm):
    #class Meta:
       # model = Robot
       # fields = ['name', 'speed', 'battery_life', 'strength']
