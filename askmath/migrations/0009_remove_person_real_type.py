# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0008_person_real_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='real_type',
        ),
    ]
