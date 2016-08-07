# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0023_auto_20160807_0525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentexperience',
            name='new_round',
        ),
    ]
