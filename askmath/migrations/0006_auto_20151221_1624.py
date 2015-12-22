# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0005_auto_20151221_1429'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Permissions',
        ),
        migrations.AlterField(
            model_name='administratorkey',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answeredquestionshistoric',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assistantkey',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='discipline',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='helpquestionshistoric',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='like',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='skippedquestionshistoric',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentexperience',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studenthistoric',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentlessonstate',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentquestionprogress',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentvideoprogress',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacherkey',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
    ]
