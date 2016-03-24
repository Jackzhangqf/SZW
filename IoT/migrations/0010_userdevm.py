# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT', '0009_auto_20160202_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDevM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20, verbose_name='\u7528\u6237')),
                ('last_name', models.CharField(max_length=20, verbose_name='\u7528\u6237')),
                ('phone', models.CharField(max_length=20, verbose_name='\u7535\u8bdd\u53f7\u7801')),
                ('job', models.CharField(max_length=50, verbose_name='\u804c\u4f4d', blank=True)),
                ('section', models.CharField(max_length=50, verbose_name='\u90e8\u95e8', blank=True)),
                ('job_unit', models.CharField(max_length=50, verbose_name='\u5355\u4f4d', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('user', models.OneToOneField(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to='IoT.RegionM')),
            ],
        ),
    ]
