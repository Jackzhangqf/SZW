# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT', '0005_auto_20160125_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilem',
            name='job_unit',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
