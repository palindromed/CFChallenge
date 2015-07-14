from django.db import models


class Robot(models.Model):

    name = models.CharField(max_length=75)
    speed = models.IntegerField(default=0)
    battery_life = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)

    def __str__(self):
        return self.name
