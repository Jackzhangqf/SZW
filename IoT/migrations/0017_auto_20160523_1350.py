# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT', '0016_auto_20160519_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorm',
            name='down_limit',
            field=models.FloatField(default=0.0, verbose_name='\u6d4b\u91cf\u4e0b\u9650'),
        ),
    ]
