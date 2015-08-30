# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
import askMathPlus.components_metro


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Choose a title for the category.', max_length=100, verbose_name='Category')),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, max_length=50, verbose_name='Color')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('person', models.ForeignKey(verbose_name='Person', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('file', models.FileField(help_text='Perform upload a file.', upload_to=b'documents/forum/comment/%Y/%m/%d', null=True, verbose_name='File', blank=True)),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['creation'],
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('person', models.ForeignKey(verbose_name='Person', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['creation'],
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Choose a title for the topic.', max_length=255, verbose_name='Category')),
                ('description', models.TextField(help_text='Choose a description for the topic.', verbose_name='Description')),
                ('file', models.FileField(help_text='Perform upload a file.', upload_to=b'documents/forum/topic/%Y/%m/%d', null=True, verbose_name='File', blank=True)),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, max_length=50, verbose_name='Color')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('category', models.ForeignKey(verbose_name='Category', to='askmath.Category')),
                ('likes', models.ManyToManyField(to='askmath.Like', null=True, verbose_name='Likes', blank=True)),
                ('person', models.ForeignKey(verbose_name='Person', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['creation'],
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(to='askmath.Like', null=True, verbose_name='Likes', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='person',
            field=models.ForeignKey(verbose_name='Person', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(verbose_name='Topic', to='askmath.Topic'),
            preserve_default=True,
        ),
    ]
