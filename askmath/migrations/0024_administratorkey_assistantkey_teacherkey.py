# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0023_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministratorKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=100, verbose_name='Key')),
                ('in_use', models.BooleanField(default=False, verbose_name='In Use')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creator', models.ForeignKey(verbose_name='Person', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='Administrator', blank=True, to='askmath.Administrator', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AssistantKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=100, verbose_name='Key')),
                ('in_use', models.BooleanField(default=False, verbose_name='In Use')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creator', models.ForeignKey(verbose_name='Person', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='Assistant', blank=True, to='askmath.Assistant', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeacherKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=100, verbose_name='Key')),
                ('in_use', models.BooleanField(default=False, verbose_name='In Use')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creator', models.ForeignKey(verbose_name='Person', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='Teacher', blank=True, to='askmath.Teacher', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
