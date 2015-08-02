# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0005_auto_20150720_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='IState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LessonAndQuestionState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scores', models.IntegerField(verbose_name='Scores')),
                ('remaining_jump', models.IntegerField(verbose_name='Remaining Jump')),
                ('hits_followed', models.IntegerField(default=0, verbose_name='Hits Followed')),
                ('errors_followed', models.IntegerField(default=0, verbose_name='Errors Followed')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('discipline', models.ForeignKey(verbose_name='Discipline', to='askmath.Discipline')),
                ('help_questions', models.ManyToManyField(related_name='Help Questions', verbose_name='Help Questions', to='askmath.Question')),
                ('lesson', models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson')),
                ('skipped_questions', models.ManyToManyField(related_name='Skipped Questions', verbose_name='Skipped Questions', to='askmath.Question')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Lesson And Question State',
                'verbose_name_plural': 'Lesson And Question States',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentState',
            fields=[
                ('istate_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='askmath.IState')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('lesson_and_question_state', models.ManyToManyField(to='askmath.LessonAndQuestionState', verbose_name='Lesson And Question State')),
                ('student', models.ForeignKey(verbose_name='Student', to='askmath.Student')),
            ],
            options={
                'ordering': ['-student'],
                'verbose_name': 'Student State',
                'verbose_name_plural': 'Student States',
            },
            bases=('askmath.istate',),
        ),
    ]
