# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0004_auto_20151007_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(help_text='Please enter you full name.', max_length=100, null=True, verbose_name='Full Name '),
            preserve_default=True,
        ),
    ]
