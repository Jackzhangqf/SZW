# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('IoT', '0003_remove_userprofilem_job_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='devm',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 25, 3, 1, 6, 604480, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regionm',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 25, 3, 1, 34, 141904, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensorm',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 25, 3, 1, 51, 102571, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccessm',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 25, 3, 2, 6, 499262, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
