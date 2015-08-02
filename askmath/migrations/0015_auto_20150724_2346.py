# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0014_video_exists'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentQuestionProgress',
            fields=[
                ('iprogress_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='askmath.IProgress')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('discipline', models.ForeignKey(verbose_name='Discipline', to='askmath.Discipline')),
                ('lesson', models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson')),
                ('question', models.ForeignKey(verbose_name='Question', to='askmath.Question')),
                ('student', models.ForeignKey(verbose_name='Student', to='askmath.Student')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Question Progress',
                'verbose_name_plural': 'Questions Progress',
            },
            bases=('askmath.iprogress',),
        ),
        migrations.CreateModel(
            name='StudentVideoProgress',
            fields=[
                ('iprogress_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='askmath.IProgress')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('discipline', models.ForeignKey(verbose_name='Discipline', to='askmath.Discipline')),
                ('lesson', models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson')),
                ('student', models.ForeignKey(verbose_name='Student', to='askmath.Student')),
                ('video', models.ForeignKey(verbose_name='Video', to='askmath.Video')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Video Progress',
                'verbose_name_plural': 'Video Progress',
            },
            bases=('askmath.iprogress',),
        ),
        migrations.RemoveField(
            model_name='questionprogress',
            name='discipline',
        ),
        migrations.RemoveField(
            model_name='questionprogress',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='questionprogress',
            name='question',
        ),
        migrations.RemoveField(
            model_name='studentprogress',
            name='iprogress_ptr',
        ),
        migrations.RemoveField(
            model_name='studentprogress',
            name='question_progress',
        ),
        migrations.DeleteModel(
            name='QuestionProgress',
        ),
        migrations.RemoveField(
            model_name='studentprogress',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentprogress',
            name='video_progress',
        ),
        migrations.DeleteModel(
            name='StudentProgress',
        ),
        migrations.RemoveField(
            model_name='videoprogress',
            name='discipline',
        ),
        migrations.RemoveField(
            model_name='videoprogress',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='videoprogress',
            name='video',
        ),
        migrations.DeleteModel(
            name='VideoProgress',
        ),
    ]
