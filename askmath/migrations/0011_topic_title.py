# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0010_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
