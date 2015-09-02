# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0012_auto_20150902_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrator',
            name='type',
            field=models.CharField(default='Administrator', max_length=50, verbose_name='Type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assistant',
            name='type',
            field=models.CharField(default='Assistant', max_length=50, verbose_name='Type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='type',
            field=models.CharField(default='Student', max_length=50, verbose_name='Type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teacher',
            name='type',
            field=models.CharField(default='Teacher', max_length=50, verbose_name='Type'),
            preserve_default=True,
        ),
    ]
