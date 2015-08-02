# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0013_item_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='exists',
            field=models.BooleanField(default=True, verbose_name='Exists'),
            preserve_default=True,
        ),
    ]
