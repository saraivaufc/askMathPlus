# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0014_auto_20150902_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(help_text='Choose a description for the category.', max_length=100, null=True, verbose_name='Description', blank=True),
            preserve_default=True,
        ),
    ]
