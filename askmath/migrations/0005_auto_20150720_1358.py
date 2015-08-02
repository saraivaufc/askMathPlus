# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0004_auto_20150720_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='answeredquestionshistoric',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='questionprogress',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studenthistoric',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studentprogress',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videoprogress',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation'),
            preserve_default=True,
        ),
    ]
