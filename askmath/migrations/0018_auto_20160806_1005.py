# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0017_auto_20160805_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentexperience',
            name='full_scores',
            field=models.IntegerField(default=0, verbose_name='Full Scores'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studentexperience',
            name='new_scores',
            field=models.IntegerField(default=0, verbose_name='New Scores'),
            preserve_default=True,
        ),
    ]
