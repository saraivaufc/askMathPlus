# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IProgress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionProgress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('discipline', models.ForeignKey(verbose_name='Discipline', to='askmath.Discipline')),
                ('lesson', models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson')),
                ('question', models.ForeignKey(verbose_name='Question', to='askmath.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentProgress',
            fields=[
                ('iprogress_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='askmath.IProgress')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('question_progress', models.ManyToManyField(to='askmath.QuestionProgress', null=True, verbose_name='Question Progress', blank=True)),
                ('student', models.ForeignKey(verbose_name='Student', to='askmath.Student')),
            ],
            options={
            },
            bases=('askmath.iprogress',),
        ),
        migrations.CreateModel(
            name='VideoProgress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('discipline', models.ForeignKey(verbose_name='Discipline', to='askmath.Discipline')),
                ('lesson', models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson')),
                ('video', models.ForeignKey(verbose_name='Question', to='askmath.Video')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='studentprogress',
            name='video_progress',
            field=models.ManyToManyField(to='askmath.VideoProgress', null=True, verbose_name='Video Progress', blank=True),
            preserve_default=True,
        ),
    ]
