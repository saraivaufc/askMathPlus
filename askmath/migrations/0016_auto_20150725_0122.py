# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0015_auto_20150724_2346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentexperience',
            options={'ordering': ['-student'], 'verbose_name': 'Student Experience', 'verbose_name_plural': 'Student Experiences'},
        ),
        migrations.RemoveField(
            model_name='studentlessonstate',
            name='answered_questions',
        ),
        migrations.AddField(
            model_name='studentlessonstate',
            name='answered_correct_questions',
            field=models.ManyToManyField(related_name='Answered Correct Questions', verbose_name='Answered Questions', to='askmath.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studentlessonstate',
            name='answered_incorrect_questions',
            field=models.ManyToManyField(related_name='Answered Incorrect Questions', verbose_name='Answered Questions', to='askmath.Question'),
            preserve_default=True,
        ),
    ]
