# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0002_auto_20150720_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnsweredQuestionsHistoric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hit', models.BooleanField(verbose_name='Hit')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('discipline', models.ForeignKey(verbose_name='Discipline', to='askmath.Discipline')),
                ('item', models.ForeignKey(verbose_name='Item', to='askmath.Item')),
                ('lesson', models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson')),
                ('question', models.ForeignKey(verbose_name='Question', to='askmath.Question')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Answered Question Historic',
                'verbose_name_plural': 'Answered Questions Historic',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IHistoric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentHistoric',
            fields=[
                ('ihistoric_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='askmath.IHistoric')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('answered_questions_historic', models.ManyToManyField(to='askmath.AnsweredQuestionsHistoric', null=True, verbose_name='Answered Questions Historic', blank=True)),
                ('student', models.ForeignKey(verbose_name='Student', to='askmath.Student')),
            ],
            options={
                'ordering': ['-student'],
                'verbose_name': 'Student Historic',
                'verbose_name_plural': 'Students Historic',
            },
            bases=('askmath.ihistoric',),
        ),
        migrations.AlterModelOptions(
            name='questionprogress',
            options={'ordering': ['-discipline'], 'verbose_name': 'Question Progress', 'verbose_name_plural': 'Questions Progress'},
        ),
        migrations.AlterModelOptions(
            name='studentprogress',
            options={'ordering': ['-student'], 'verbose_name': 'Student Progress', 'verbose_name_plural': 'Students Progress'},
        ),
        migrations.AlterModelOptions(
            name='videoprogress',
            options={'ordering': ['-discipline'], 'verbose_name': 'Video Progress', 'verbose_name_plural': 'Video Progress'},
        ),
        migrations.AlterField(
            model_name='videoprogress',
            name='video',
            field=models.ForeignKey(verbose_name='Video', to='askmath.Video'),
            preserve_default=True,
        ),
    ]
