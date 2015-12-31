# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0003_auto_20151231_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='responsible',
            field=models.ForeignKey(related_name='Responsible', verbose_name='Respons\xe1vel', to='askmath.Teacher', help_text='Escolha uma respons\xe1vel para a disciplina.'),
            preserve_default=True,
        ),
    ]
