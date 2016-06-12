# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0006_auto_20160611_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='disciplines',
            field=models.ManyToManyField(help_text='Choose disciplines that this classe.', to='askmath.Discipline', null=True, verbose_name='Disciplinas', blank=True),
            preserve_default=True,
        ),
    ]
