# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0009_auto_20150901_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default=1, help_text='Choose a description for the category.', max_length=100, verbose_name='Description'),
            preserve_default=False,
        ),
    ]
