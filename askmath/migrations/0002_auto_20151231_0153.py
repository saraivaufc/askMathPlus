# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Discipline',
            name='responsible',
            field=models.ForeignKey(verbose_name='Respons\xe1vel', to=settings.AUTH_USER_MODEL, help_text='Escolha uma respons\xe1vel para a disciplina.'),
            preserve_default=True,
        ),
    ]
