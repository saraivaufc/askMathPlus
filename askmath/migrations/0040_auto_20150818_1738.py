# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0039_auto_20150817_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='scores',
            field=models.IntegerField(verbose_name='Scores', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
            preserve_default=True,
        ),
    ]
