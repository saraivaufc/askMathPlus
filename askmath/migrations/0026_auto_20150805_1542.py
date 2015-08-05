# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0025_auto_20150805_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administratorkey',
            name='key',
            field=models.CharField(unique=True, max_length=100, verbose_name='Key'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assistantkey',
            name='key',
            field=models.CharField(unique=True, max_length=100, verbose_name='Key'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacherkey',
            name='key',
            field=models.CharField(unique=True, max_length=100, verbose_name='Key'),
            preserve_default=True,
        ),
    ]
