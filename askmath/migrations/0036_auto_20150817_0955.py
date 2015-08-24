# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0035_auto_20150817_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(help_text='Enter your Password', max_length=128, verbose_name='Password'),
            preserve_default=True,
        ),
    ]
