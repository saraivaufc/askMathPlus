# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0008_iexperience_studentexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentLessonState',
            fields=[
                ('istate_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='askmath.IState')),
                ('scores', models.IntegerField(default=0, verbose_name='Scores')),
                ('remaining_jump', models.IntegerField(default=0, verbose_name='Remaining Jump')),
                ('hits_followed', models.IntegerField(default=0, verbose_name='Hits Followed')),
                ('errors_followed', models.IntegerField(default=0, verbose_name='Errors Followed')),
                ('percentage_completed', models.IntegerField(default=0, verbose_name='Percentage Completed')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('answered_questions', models.ManyToManyField(related_name='Answered Questions', verbose_name='Answered Questions', to='askmath.Question')),
                ('discipline', models.ForeignKey(verbose_name='Discipline', to='askmath.Discipline')),
                ('help_questions', models.ManyToManyField(related_name='Help Questions', verbose_name='Help Questions', to='askmath.Question')),
                ('lesson', models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson')),
                ('skipped_questions', models.ManyToManyField(related_name='Skipped Questions', verbose_name='Skipped Questions', to='askmath.Question')),
                ('student', models.ForeignKey(verbose_name='Student', to='askmath.Student')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Lesson And Question State',
                'verbose_name_plural': 'Lesson And Question States',
            },
            bases=('askmath.istate',),
        ),
        migrations.RemoveField(
            model_name='lessonandquestionstate',
            name='discipline',
        ),
        migrations.RemoveField(
            model_name='lessonandquestionstate',
            name='help_questions',
        ),
        migrations.RemoveField(
            model_name='lessonandquestionstate',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='lessonandquestionstate',
            name='skipped_questions',
        ),
        migrations.RemoveField(
            model_name='studentstate',
            name='istate_ptr',
        ),
        migrations.RemoveField(
            model_name='studentstate',
            name='lesson_and_question_state',
        ),
        migrations.DeleteModel(
            name='LessonAndQuestionState',
        ),
        migrations.RemoveField(
            model_name='studentstate',
            name='student',
        ),
        migrations.DeleteModel(
            name='StudentState',
        ),
    ]
