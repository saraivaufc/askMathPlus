# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0005_auto_20150829_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(help_text='Choose a title for the category.', max_length=100, verbose_name='Title'),
            preserve_default=True,
        ),
    ]
