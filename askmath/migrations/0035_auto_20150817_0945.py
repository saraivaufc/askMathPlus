# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0034_auto_20150816_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='responsible',
            field=models.CharField(help_text='Choose responsible for the discipline.', max_length=100, null=True, verbose_name='Responsible', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='discipline',
            name='title',
            field=models.CharField(help_text='Choose a title for the discipline.', max_length=100, verbose_name='Title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(help_text='Choose a description for item is.', verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(help_text='Choose a description for lesson is.', verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='disciplines',
            field=models.ManyToManyField(help_text='Choose the disciplines which is lesson belongs.', to='askmath.Discipline', verbose_name='Disciplines'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='maximum_hops',
            field=models.IntegerField(help_text='Choose the maximum number of hops that the student can perform this lesson.', verbose_name='Maximum Hops'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(help_text='Choose a title for lesson is.', max_length=50, verbose_name='Title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(help_text='Enter your email.', unique=True, max_length=254, verbose_name='Email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(help_text='Enter your name.', max_length=100, null=True, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(help_text='Enter your Username', unique=True, max_length=30, verbose_name='Username', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(help_text='Choose a description for question is.', verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='lesson',
            field=models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson', help_text='Choose the lesson which is question belongs.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='scores',
            field=models.IntegerField(verbose_name='Scores'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(help_text='Perform upload a file.', upload_to=b'documents/video/%Y/%m/%d', verbose_name='File'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='lesson',
            field=models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson', help_text='Choose the lesson which is video belongs.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(help_text='Choose a title for video is.', max_length=50, verbose_name='Title'),
            preserve_default=True,
        ),
    ]
