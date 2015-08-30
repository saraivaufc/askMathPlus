# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0004_auto_20150828_0442'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-creation'], 'verbose_name': 'Topic', 'verbose_name_plural': 'Topics'},
        ),
        migrations.RemoveField(
            model_name='topic',
            name='title',
        ),
    ]
