# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0013_auto_20150902_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrator',
            name='type',
        ),
        migrations.RemoveField(
            model_name='assistant',
            name='type',
        ),
        migrations.RemoveField(
            model_name='student',
            name='type',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='type',
        ),
    ]
