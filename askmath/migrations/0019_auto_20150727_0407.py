# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0018_auto_20150727_0151'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpQuestionsHistoric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('discipline', models.ForeignKey(verbose_name='Discipline', to='askmath.Discipline')),
                ('lesson', models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson')),
                ('question', models.ForeignKey(verbose_name='Question', to='askmath.Question')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Help Question Historic',
                'verbose_name_plural': 'Help Questions Historic',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkippedQuestionsHistoric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('discipline', models.ForeignKey(verbose_name='Discipline', to='askmath.Discipline')),
                ('lesson', models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson')),
                ('question', models.ForeignKey(verbose_name='Question', to='askmath.Question')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Skipped Question Historic',
                'verbose_name_plural': 'Skipped Questions Historic',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='studenthistoric',
            name='help_questions_historic',
            field=models.ManyToManyField(related_name='Help Question Historic', null=True, verbose_name='Answered Questions Historic', to='askmath.HelpQuestionsHistoric', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studenthistoric',
            name='skipped_questions_historic',
            field=models.ManyToManyField(related_name='Skipped Question Historic', null=True, verbose_name='Answered Questions Historic', to='askmath.SkippedQuestionsHistoric', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studenthistoric',
            name='answered_questions_historic',
            field=models.ManyToManyField(related_name='Answered Questions Historic', null=True, verbose_name='Answered Questions Historic', to='askmath.AnsweredQuestionsHistoric', blank=True),
            preserve_default=True,
        ),
    ]
