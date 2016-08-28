# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0031_auto_20160820_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(null=True, default=None, max_length=254, blank=True, help_text='Please enter you email.', unique=True, verbose_name='Email'),
            preserve_default=True,
        ),
    ]
