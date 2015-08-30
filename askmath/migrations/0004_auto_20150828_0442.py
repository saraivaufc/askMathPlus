# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0003_auto_20150828_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(help_text='Choose a title for the category.', unique=True, max_length=100, verbose_name='Title'),
            preserve_default=True,
        ),
    ]
