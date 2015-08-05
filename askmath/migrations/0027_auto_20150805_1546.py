# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import askmath.models.access.registerkey


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0026_auto_20150805_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administratorkey',
            name='key',
            field=models.CharField(default=askmath.models.access.registerkey.generate_key, max_length=100, verbose_name='Key'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assistantkey',
            name='key',
            field=models.CharField(default=askmath.models.access.registerkey.generate_key, max_length=100, verbose_name='Key'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacherkey',
            name='key',
            field=models.CharField(default=askmath.models.access.registerkey.generate_key, max_length=100, verbose_name='Key'),
            preserve_default=True,
        ),
    ]
