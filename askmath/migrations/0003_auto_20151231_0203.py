# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0002_auto_20151231_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='responsible',
            field=models.ForeignKey(related_name='Responsible', to='askmath.Teacher', help_text='Escolha uma respons\xe1vel para a disciplina.'),
            preserve_default=True,
        ),
    ]
