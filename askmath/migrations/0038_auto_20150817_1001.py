# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0037_auto_20150817_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(help_text='Please enter you email.', unique=True, max_length=254, verbose_name='Email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(help_text='Please enter you name.', max_length=100, null=True, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(help_text='Please enter you username.', unique=True, max_length=30, verbose_name='Username', db_index=True),
            preserve_default=True,
        ),
    ]
