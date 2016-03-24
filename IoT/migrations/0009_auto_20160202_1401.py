# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('IoT', '0008_auto_20160126_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensorthresholdm',
            name='sensor',
        ),
        migrations.AlterField(
            model_name='datam',
            name='data',
            field=models.FloatField(verbose_name='\u6570\u636e'),
        ),
        migrations.AlterField(
            model_name='datam',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u91c7\u96c6\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='datam',
            name='sensor',
            field=models.ForeignKey(verbose_name='\u6570\u636e\u6240\u5c5e\u8bbe\u5907', to='IoT.SensorM'),
        ),
        migrations.AlterField(
            model_name='devm',
            name='access_key',
            field=models.CharField(max_length=32, verbose_name='\u8bbf\u95eeKey', blank=True),
        ),
        migrations.AlterField(
            model_name='devm',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u4fee\u6539\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='devm',
            name='dev_id',
            field=models.PositiveIntegerField(verbose_name='\u8bbe\u5907\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='devm',
            name='dev_info',
            field=models.CharField(max_length=200, verbose_name='\u8bbe\u5907\u63cf\u8ff0', blank=True),
        ),
        migrations.AlterField(
            model_name='devm',
            name='dev_name',
            field=models.CharField(max_length=50, verbose_name='\u8bbe\u5907\u540d\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='devm',
            name='region',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u533a\u57df', to='IoT.RegionM'),
        ),
        migrations.AlterField(
            model_name='regionm',
            name='access_key',
            field=models.CharField(max_length=32, verbose_name='\u8bbf\u95eeKey', blank=True),
        ),
        migrations.AlterField(
            model_name='regionm',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u4fee\u6539\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='regionm',
            name='region_id',
            field=models.PositiveIntegerField(verbose_name=b'\xe5\x8c\xba\xe5\x9f\x9f\xe7\xbc\x96\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='regionm',
            name='region_info',
            field=models.CharField(max_length=50, verbose_name='\u533a\u57df\u63cf\u8ff0', blank=True),
        ),
        migrations.AlterField(
            model_name='regionm',
            name='region_name',
            field=models.CharField(max_length=50, verbose_name='\u533a\u57df\u540d\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='regionm',
            name='reserved',
            field=models.CharField(max_length=50, verbose_name='\u4fdd\u7559\u9879', blank=True),
        ),
        migrations.AlterField(
            model_name='sensorm',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u4fee\u6539\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='sensorm',
            name='dev',
            field=models.ForeignKey(verbose_name='\u4f20\u611f\u5668\u6240\u5c5e\u8bbe\u5907', to='IoT.DevM'),
        ),
        migrations.AlterField(
            model_name='sensorm',
            name='sensor_id',
            field=models.PositiveIntegerField(verbose_name='\u4f20\u611f\u5668\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='sensorm',
            name='sensor_info',
            field=models.CharField(max_length=200, verbose_name='\u4f20\u611f\u5668\u63cf\u8ff0', blank=True),
        ),
        migrations.AlterField(
            model_name='sensorm',
            name='sensor_name',
            field=models.CharField(max_length=50, verbose_name='\u4f20\u611f\u5668\u540d\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='sensorm',
            name='sensor_type',
            field=models.CharField(max_length=10, verbose_name='\u4f20\u611f\u5668\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='sensorthresholdm',
            name='threshold_e',
            field=models.BooleanField(default=False, verbose_name='\u4f7f\u80fd\u4f4d'),
        ),
        migrations.AlterField(
            model_name='sensorthresholdm',
            name='threshold_h',
            field=models.DecimalField(default=1000, verbose_name='\u4e0a\u9650\u503c', max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='sensorthresholdm',
            name='threshold_l',
            field=models.DecimalField(default=0, verbose_name='\u4e0b\u9650\u503c', max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='sensorthresholdm',
            name='useraccess',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u8bbf\u95ee\u6743\u9650\u6587\u4ef6', to='IoT.UserAccessM'),
        ),
        migrations.AlterField(
            model_name='useraccessm',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u4fee\u6539\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='useraccessm',
            name='dev_id',
            field=models.BigIntegerField(verbose_name='\u8bbe\u5907\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='useraccessm',
            name='permission_c',
            field=models.BooleanField(default=False, verbose_name='\u63a7\u5236\u6743\u9650'),
        ),
        migrations.AlterField(
            model_name='useraccessm',
            name='permission_r',
            field=models.BooleanField(default=False, verbose_name='\u8bfb\u6743\u9650'),
        ),
        migrations.AlterField(
            model_name='useraccessm',
            name='permission_w',
            field=models.BooleanField(default=False, verbose_name='\u5199\u6743\u9650'),
        ),
        migrations.AlterField(
            model_name='useraccessm',
            name='region_access_key',
            field=models.CharField(max_length=40, verbose_name='\u5bc6\u94a5'),
        ),
        migrations.AlterField(
            model_name='useraccessm',
            name='region_id',
            field=models.SmallIntegerField(verbose_name='\u533a\u57df\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='useraccessm',
            name='region_or_dev_flag',
            field=models.BooleanField(verbose_name='\u533a\u57df'),
        ),
        migrations.AlterField(
            model_name='useraccessm',
            name='user',
            field=models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofilem',
            name='job',
            field=models.CharField(max_length=50, verbose_name='\u804c\u4f4d', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofilem',
            name='job_unit',
            field=models.CharField(max_length=50, verbose_name='\u5355\u4f4d', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofilem',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='\u7535\u8bdd\u53f7\u7801'),
        ),
        migrations.AlterField(
            model_name='userprofilem',
            name='section',
            field=models.CharField(max_length=50, verbose_name='\u90e8\u95e8', blank=True),
        ),
    ]
