# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('IoT', '0013_auto_20160224_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensorthresholdm',
            name='useraccess',
        ),
        migrations.AddField(
            model_name='sensorthresholdm',
            name='sensor_id',
            field=models.IntegerField(default=0, verbose_name='\u4f20\u611f\u5668\u7f16\u53f7'),
        ),
        migrations.AddField(
            model_name='sensorthresholdm',
            name='user',
            field=models.ForeignKey(default=1, verbose_name='\u6240\u5c5e\u8bbf\u95ee\u6743\u9650\u6587\u4ef6', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
