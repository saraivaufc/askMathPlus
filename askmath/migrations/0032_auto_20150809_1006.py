# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0031_auto_20150809_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='disciplines',
            field=models.ManyToManyField(help_text='Choose the disciplines which is lesson belongs.', to='askmath.Discipline', verbose_name='Disciplines'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='position',
            field=models.IntegerField(default=1, help_text='Choose the position which is question belongs.', verbose_name='Position'),
            preserve_default=False,
        ),
    ]
