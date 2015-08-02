# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0009_auto_20150722_1650'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentlessonstate',
            options={'ordering': ['-discipline'], 'verbose_name': 'Student Lesson State', 'verbose_name_plural': 'Students Lessons State'},
        ),
        migrations.RemoveField(
            model_name='answeredquestionshistoric',
            name='exists',
        ),
        migrations.RemoveField(
            model_name='discipline',
            name='exists',
        ),
        migrations.RemoveField(
            model_name='item',
            name='exists',
        ),
        migrations.RemoveField(
            model_name='item',
            name='is_correct',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='exists',
        ),
        migrations.RemoveField(
            model_name='person',
            name='exists',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_administrator',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_moderator',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='question',
            name='exists',
        ),
        migrations.RemoveField(
            model_name='questionprogress',
            name='exists',
        ),
        migrations.RemoveField(
            model_name='studentexperience',
            name='exists',
        ),
        migrations.RemoveField(
            model_name='studenthistoric',
            name='exists',
        ),
        migrations.RemoveField(
            model_name='studentlessonstate',
            name='exists',
        ),
        migrations.RemoveField(
            model_name='studentprogress',
            name='exists',
        ),
        migrations.RemoveField(
            model_name='video',
            name='exists',
        ),
        migrations.RemoveField(
            model_name='video',
            name='video',
        ),
        migrations.RemoveField(
            model_name='videoprogress',
            name='exists',
        ),
        migrations.AddField(
            model_name='video',
            name='file',
            field=models.FileField(default=None, help_text='Perform upload a file.', verbose_name='File', upload_to=b'documents/video/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
