# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT', '0014_auto_20160224_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='devm',
            name='dev_position',
            field=models.CharField(max_length=100, verbose_name='GPS\u5750\u6807', blank=True),
        ),
        migrations.AddField(
            model_name='devm',
            name='enable',
            field=models.BooleanField(default=False, verbose_name='\u8bbe\u5907\u4f7f\u80fd\u4f4d'),
        ),
        migrations.AddField(
            model_name='devm',
            name='reserved',
            field=models.CharField(max_length=100, verbose_name='\u4fdd\u7559\u98791', blank=True),
        ),
        migrations.AddField(
            model_name='devm',
            name='reserved2',
            field=models.CharField(max_length=100, verbose_name='\u4fdd\u7559\u98792', blank=True),
        ),
        migrations.AddField(
            model_name='regionm',
            name='enable',
            field=models.BooleanField(default=False, verbose_name='\u533a\u57df\u4f7f\u80fd\u4f4d'),
        ),
        migrations.AddField(
            model_name='regionm',
            name='region_position',
            field=models.CharField(max_length=100, verbose_name='GPS\u5750\u6807', blank=True),
        ),
        migrations.AddField(
            model_name='regionm',
            name='reserved2',
            field=models.CharField(max_length=100, verbose_name='\u4fdd\u7559\u98792', blank=True),
        ),
        migrations.AddField(
            model_name='sensorm',
            name='data_scale',
            field=models.FloatField(default=1, verbose_name='\u6570\u636e\u6807\u5ea6'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensorm',
            name='data_symbol',
            field=models.CharField(default=' ', max_length=20, verbose_name='\u6570\u636e\u7b26\u53f7', choices=[(b'A', '\u5b89\u57f9'), (b'kA', '\u5343\u5b89\u57f9'), (b'V', '\u4f0f\u7279'), (b'kV', '\u5343\u4f0f\u7279'), (b'\xe2\x84\x83', '\u6444\u6c0f\u5ea6'), (b'%', '\u767e\u5206\u6570'), (b'MPa', '\u5146\u5e15'), (b'kPa', '\u5343\u5e15'), (b'Pa', '\u5e15'), (b'\xe7\xbb\x8f\xe7\xba\xac\xe5\xba\xa6', '\u7ecf\u7eac\u5ea6'), (b' ', '\u65e0')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensorm',
            name='enable',
            field=models.BooleanField(default=False, verbose_name='\u4f20\u611f\u5668\u4f7f\u80fd\u4f4d'),
        ),
        migrations.AddField(
            model_name='sensorm',
            name='reserved',
            field=models.CharField(max_length=100, verbose_name='\u4fdd\u7559\u98791', blank=True),
        ),
        migrations.AddField(
            model_name='sensorm',
            name='reserved2',
            field=models.CharField(max_length=100, verbose_name='\u4fdd\u7559\u98792', blank=True),
        ),
        migrations.AddField(
            model_name='sensorm',
            name='sensor_position',
            field=models.CharField(max_length=100, verbose_name='GPS\u5750\u6807', blank=True),
        ),
        migrations.AddField(
            model_name='userdevm',
            name='reserved',
            field=models.CharField(max_length=100, verbose_name='\u4fdd\u7559\u98791', blank=True),
        ),
        migrations.AddField(
            model_name='userdevm',
            name='reserved2',
            field=models.CharField(max_length=100, verbose_name='\u4fdd\u7559\u98792', blank=True),
        ),
        migrations.AlterField(
            model_name='regionm',
            name='reserved',
            field=models.CharField(max_length=100, verbose_name='\u4fdd\u7559\u98791', blank=True),
        ),
        migrations.AlterField(
            model_name='sensorm',
            name='sensor_type',
            field=models.CharField(max_length=10, verbose_name='\u4f20\u611f\u5668\u7c7b\u578b', choices=[(b'A', '\u7535\u6d41'), (b'V', '\u7535\u538b'), (b'T', '\u6e29\u5ea6'), (b'H', '\u6e7f\u5ea6'), (b'P', '\u538b\u529b'), (b'L', '\u4f4d\u7f6e'), (b'Y', '\u65f6\u95f4'), (b'F', '\u6587\u4ef6'), (b'I', '\u6d88\u606f'), (b'J', '\u56fe\u7247')]),
        ),
    ]
