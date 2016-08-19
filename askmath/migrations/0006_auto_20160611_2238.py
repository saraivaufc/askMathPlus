# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0005_auto_20160611_2135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classe',
            options={'ordering': ['name'], 'verbose_name': 'Turma', 'verbose_name_plural': 'Turmas'},
        ),
        migrations.AlterField(
            model_name='classe',
            name='plan',
            field=models.FileField(help_text='Realize upload de um arquivo.', upload_to=b'documents/plans/%Y/%m/%d', null=True, verbose_name='Plano de Aula', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classe',
            name='semester',
            field=models.FloatField(help_text='Choose semester of this classe.', verbose_name='Semestre'),
            preserve_default=True,
        ),
    ]
