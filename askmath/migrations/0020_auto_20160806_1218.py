# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0019_auto_20160806_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentexperience',
            name='round',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Round'),
            preserve_default=True,
        ),
    ]
