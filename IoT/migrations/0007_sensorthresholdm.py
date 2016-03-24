# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT', '0006_userprofilem_job_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorThresholdM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('threshold_h', models.DecimalField(default=1000, max_digits=6, decimal_places=2)),
                ('threshold_l', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('threshold_e', models.BooleanField(default=False)),
                ('sensor', models.ForeignKey(to='IoT.SensorM')),
                ('useraccess', models.ForeignKey(to='IoT.UserAccessM')),
            ],
        ),
    ]
