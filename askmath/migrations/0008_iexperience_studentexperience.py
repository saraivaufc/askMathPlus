# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0007_auto_20150721_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='IExperience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentExperience',
            fields=[
                ('iexperience_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='askmath.IExperience')),
                ('scores', models.IntegerField(default=0, verbose_name='Scores')),
                ('level', models.IntegerField(default=1, verbose_name='Level')),
                ('stars', models.IntegerField(default=0, verbose_name='Stars')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True)),
                ('student', models.ForeignKey(verbose_name='Student', to='askmath.Student')),
            ],
            options={
                'ordering': ['-student'],
                'verbose_name': 'StudentExperience',
                'verbose_name_plural': 'StudentExperiences',
            },
            bases=('askmath.iexperience',),
        ),
    ]
