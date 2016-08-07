# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0022_studentexperience_new_round'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentexperience',
            name='full_scores',
        ),
        migrations.AddField(
            model_name='studentexperience',
            name='last_new_scores',
            field=models.IntegerField(default=0, verbose_name='Last New Scores'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studentexperience',
            name='last_scores',
            field=models.IntegerField(default=0, verbose_name='Last Scores'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentexperience',
            name='student',
            field=models.ForeignKey(verbose_name='Estudante', to='askmath.Student', unique=True),
            preserve_default=True,
        ),
    ]
