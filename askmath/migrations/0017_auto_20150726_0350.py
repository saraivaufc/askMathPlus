# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0016_auto_20150725_0122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discipline',
            options={'ordering': ['title'], 'verbose_name': 'Discipline', 'verbose_name_plural': 'Disciplines'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['title'], 'verbose_name': 'Lesson', 'verbose_name_plural': 'Lessons'},
        ),
        migrations.AddField(
            model_name='studentexperience',
            name='max_scores',
            field=models.IntegerField(default=30, verbose_name='Max Scores'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentlessonstate',
            name='answered_correct_questions',
            field=models.ManyToManyField(related_name='Answered Correct Questions', null=True, verbose_name='Answered Questions', to='askmath.Question', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentlessonstate',
            name='answered_incorrect_questions',
            field=models.ManyToManyField(related_name='Answered Incorrect Questions', null=True, verbose_name='Answered Questions', to='askmath.Question', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentlessonstate',
            name='help_questions',
            field=models.ManyToManyField(related_name='Help Questions', null=True, verbose_name='Help Questions', to='askmath.Question', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentlessonstate',
            name='skipped_questions',
            field=models.ManyToManyField(related_name='Skipped Questions', null=True, verbose_name='Skipped Questions', to='askmath.Question', blank=True),
            preserve_default=True,
        ),
    ]
