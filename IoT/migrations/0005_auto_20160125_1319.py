# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('IoT', '0004_auto_20160125_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datam',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='devm',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='regionm',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='sensorm',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='useraccessm',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='useraccessm',
            name='permission_c',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='useraccessm',
            name='permission_r',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='useraccessm',
            name='permission_w',
            field=models.BooleanField(default=False),
        ),
    ]
