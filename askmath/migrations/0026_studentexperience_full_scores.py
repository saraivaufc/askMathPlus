# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0025_auto_20160807_0602'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentexperience',
            name='full_scores',
            field=models.IntegerField(default=0, verbose_name='Full Scores'),
            preserve_default=True,
        ),
    ]
