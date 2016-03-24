# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccessM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region_or_dev_flag', models.BooleanField()),
                ('region_access_key', models.CharField(max_length=40)),
                ('region_id', models.SmallIntegerField()),
                ('dev_id', models.BigIntegerField()),
                ('permission_w', models.BooleanField()),
                ('permission_r', models.BooleanField()),
                ('permission_c', models.BooleanField()),
                ('user', models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=20)),
                ('job', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=50)),
                ('job_unit', models.CharField(max_length=50)),
                ('user', models.OneToOneField(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
