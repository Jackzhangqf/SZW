# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT', '0007_sensorthresholdm'),
    ]

    operations = [
        migrations.AddField(
            model_name='devm',
            name='access_key',
            field=models.CharField(max_length=32, blank=True),
        ),
        migrations.AddField(
            model_name='regionm',
            name='access_key',
            field=models.CharField(max_length=32, blank=True),
        ),
    ]
