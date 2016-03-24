# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT', '0010_userdevm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdevm',
            name='user',
        ),
        migrations.AddField(
            model_name='userdevm',
            name='user',
            field=models.ManyToManyField(to='IoT.RegionM', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7'),
        ),
    ]
