# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answeredquestionshistoric',
            options={'ordering': ['-creation'], 'verbose_name': 'Hist\xf3rico da Quest\xe3o Resolvida', 'verbose_name_plural': 'Hist\xf3rico de Quest\xf5es Resolvidas'},
        ),
        migrations.AlterField(
            model_name='studentexperience',
            name='student',
            field=models.ForeignKey(verbose_name='Pessoa', to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentlessonstate',
            name='student',
            field=models.ForeignKey(verbose_name='Pessoa', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
