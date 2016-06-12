# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0002_auto_20160611_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discipline',
            name='classe',
        ),
        migrations.AddField(
            model_name='classe',
            name='disciplines',
            field=models.ManyToManyField(help_text='Choose disciplines that this classe.', to='askmath.Discipline', verbose_name='Disciplinas'),
            preserve_default=True,
        ),
    ]
