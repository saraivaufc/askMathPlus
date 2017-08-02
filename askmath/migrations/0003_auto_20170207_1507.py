# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0002_auto_20161118_2358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discipline',
            options={'ordering': ['title'], 'verbose_name': 'Conte\xfado', 'verbose_name_plural': 'Conte\xfado'},
        ),
    ]
