# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0027_studentexperience_date_new_round'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentexperience',
            name='date_new_round',
        ),
        migrations.AddField(
            model_name='studentexperience',
            name='date_end_new_round',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date End New Round'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studentexperience',
            name='date_start_new_round',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Start New Round'),
            preserve_default=True,
        ),
    ]
