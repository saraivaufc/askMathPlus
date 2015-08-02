# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0021_auto_20150727_0931'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={},
        ),
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(help_text='Required. 30 characters or fewer.', unique=True, max_length=30, verbose_name='Username', db_index=True),
            preserve_default=True,
        ),
    ]
