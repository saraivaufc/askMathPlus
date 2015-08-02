# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0017_auto_20150726_0350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='person',
            name='lastname',
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(unique=True, max_length=254, verbose_name='Email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Enter a valid username.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters', unique=True, verbose_name='Username', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentexperience',
            name='max_scores',
            field=models.IntegerField(default=10, verbose_name='Max Scores'),
            preserve_default=True,
        ),
    ]
