# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0024_remove_studentexperience_new_round'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentexperience',
            name='last_winner',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studentexperience',
            name='new_round',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
