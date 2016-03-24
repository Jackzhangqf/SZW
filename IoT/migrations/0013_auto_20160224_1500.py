# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT', '0012_auto_20160218_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensorthresholdm',
            name='threshold_h',
        ),
        migrations.RemoveField(
            model_name='sensorthresholdm',
            name='threshold_l',
        ),
        migrations.RemoveField(
            model_name='userdevm',
            name='job',
        ),
        migrations.RemoveField(
            model_name='userdevm',
            name='job_unit',
        ),
        migrations.RemoveField(
            model_name='userdevm',
            name='region',
        ),
        migrations.RemoveField(
            model_name='userdevm',
            name='section',
        ),
        migrations.AddField(
            model_name='devm',
            name='dev_sn',
            field=models.CharField(max_length=48, verbose_name='\u8bbe\u5907\u5e8f\u5217\u53f7', blank=True),
        ),
        migrations.AddField(
            model_name='sensorthresholdm',
            name='threshold',
            field=models.DecimalField(default=10, verbose_name='\u9650\u503c', max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='sensorthresholdm',
            name='threshold_flag',
            field=models.BooleanField(default=True, verbose_name='\u9650\u503c\u6807\u5fd7'),
        ),
        migrations.AddField(
            model_name='userdevm',
            name='useraccess',
            field=models.ManyToManyField(to='IoT.UserAccessM', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7'),
        ),
        migrations.AlterField(
            model_name='devm',
            name='dev_id',
            field=models.PositiveIntegerField(unique=True, verbose_name='\u8bbe\u5907\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='regionm',
            name='region_id',
            field=models.PositiveIntegerField(unique=True, verbose_name=b'\xe5\x8c\xba\xe5\x9f\x9f\xe7\xbc\x96\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='sensorm',
            name='sensor_id',
            field=models.PositiveIntegerField(unique=True, verbose_name='\u4f20\u611f\u5668\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='userdevm',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='\u7528\u6237\u540d'),
        ),
        migrations.AlterField(
            model_name='userdevm',
            name='last_name',
            field=models.CharField(max_length=20, verbose_name='\u7528\u6237\u59d3'),
        ),
    ]
