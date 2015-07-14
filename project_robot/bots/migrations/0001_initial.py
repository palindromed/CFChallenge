# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('speed', models.IntegerField(default=0)),
                ('battery_life', models.IntegerField(default=0)),
                ('strength', models.IntegerField(default=0)),
            ],
        ),
    ]
