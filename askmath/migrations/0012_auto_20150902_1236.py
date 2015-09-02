# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0011_topic_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(help_text='Choose a description for the category.', max_length=100, verbose_name='Description'),
            preserve_default=True,
        ),
    ]
