# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT', '0011_auto_20160218_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdevm',
            old_name='user',
            new_name='region',
        ),
    ]
