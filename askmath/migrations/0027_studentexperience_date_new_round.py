# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0026_studentexperience_full_scores'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentexperience',
            name='date_new_round',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date New Round'),
            preserve_default=True,
        ),
    ]
