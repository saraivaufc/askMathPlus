# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0002_auto_20160102_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administratorkey',
            name='creator',
            field=models.ForeignKey(verbose_name='Criador', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assistantkey',
            name='creator',
            field=models.ForeignKey(verbose_name='Criador', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='person',
            field=models.ForeignKey(verbose_name='Pessoa', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='person',
            field=models.ForeignKey(verbose_name='Person', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='like',
            name='person',
            field=models.ForeignKey(verbose_name='Pessoa', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacherkey',
            name='creator',
            field=models.ForeignKey(verbose_name='Criador', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='person',
            field=models.ForeignKey(verbose_name='Pessoa', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
