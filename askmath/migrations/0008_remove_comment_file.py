# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0007_auto_20150901_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='file',
        ),
    ]
