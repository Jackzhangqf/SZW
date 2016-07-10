# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT', '0015_auto_20160519_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensorm',
            name='down_limit',
            field=models.FloatField(default=100.0, verbose_name='\u6d4b\u91cf\u4e0b\u9650'),
        ),
        migrations.AddField(
            model_name='sensorm',
            name='top_limit',
            field=models.FloatField(default=100.0, verbose_name='\u6d4b\u91cf\u4e0a\u9650'),
        ),
        migrations.AlterField(
            model_name='sensorm',
            name='data_symbol',
            field=models.CharField(max_length=20, verbose_name='\u6570\u636e\u7b26\u53f7', choices=[('A', '\u5b89\u57f9'), ('kA', '\u5343\u5b89\u57f9'), ('V', '\u4f0f\u7279'), ('kV', '\u5343\u4f0f\u7279'), ('\u2103', '\u6444\u6c0f\u5ea6'), ('%', '\u767e\u5206\u6570'), ('MPa', '\u5146\u5e15'), ('kPa', '\u5343\u5e15'), ('Pa', '\u5e15'), ('\u7ecf\u7eac\u5ea6', '\u7ecf\u7eac\u5ea6'), (b' ', '\u65e0')]),
        ),
    ]
