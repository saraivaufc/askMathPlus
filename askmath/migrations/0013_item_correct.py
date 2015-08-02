# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0012_auto_20150723_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='correct',
            field=models.BooleanField(default=False, help_text='Say if this item is correct.', verbose_name='Is Correct'),
            preserve_default=True,
        ),
    ]
