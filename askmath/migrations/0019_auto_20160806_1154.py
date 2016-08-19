# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0018_auto_20160806_1005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentexperience',
            options={'ordering': ['creation'], 'verbose_name': 'Experi\xeancia do Estudante', 'verbose_name_plural': 'Experi\xeancias dos Estudantes'},
        ),
        migrations.AddField(
            model_name='studentexperience',
            name='round',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Round'),
            preserve_default=True,
        ),
    ]
