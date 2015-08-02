# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0006_istate_lessonandquestionstate_studentstate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonandquestionstate',
            name='remaining_jump',
            field=models.IntegerField(default=0, verbose_name='Remaining Jump'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lessonandquestionstate',
            name='scores',
            field=models.IntegerField(default=0, verbose_name='Scores'),
            preserve_default=True,
        ),
    ]
