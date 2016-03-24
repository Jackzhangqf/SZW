# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time', models.DateTimeField()),
                ('data', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DevM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dev_id', models.PositiveIntegerField()),
                ('dev_info', models.CharField(max_length=200, blank=True)),
                ('dev_name', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegionM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region_id', models.PositiveIntegerField(verbose_name=b'region')),
                ('region_info', models.CharField(max_length=50, blank=True)),
                ('region_name', models.CharField(max_length=50, blank=True)),
                ('reserved', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SensorM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sensor_id', models.PositiveIntegerField()),
                ('sensor_info', models.CharField(max_length=200, blank=True)),
                ('sensor_type', models.CharField(max_length=10)),
                ('sensor_name', models.CharField(max_length=50, blank=True)),
                ('dev', models.ForeignKey(to='IoT.DevM')),
            ],
        ),
        migrations.AlterField(
            model_name='userprofilem',
            name='job',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofilem',
            name='job_unit',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofilem',
            name='section',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='devm',
            name='region',
            field=models.ForeignKey(to='IoT.RegionM'),
        ),
        migrations.AddField(
            model_name='datam',
            name='sensor',
            field=models.ForeignKey(to='IoT.SensorM'),
        ),
    ]
