# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0036_auto_20150817_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
            preserve_default=True,
        ),
    ]
