# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0011_person_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='answeredquestionshistoric',
            name='exists',
            field=models.BooleanField(default=True, verbose_name='Exists'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discipline',
            name='exists',
            field=models.BooleanField(default=True, verbose_name='Exists'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='exists',
            field=models.BooleanField(default=True, verbose_name='Exists'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='exists',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='exists',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='is_administrator',
            field=models.BooleanField(default=False, verbose_name='administrator status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='is_moderator',
            field=models.BooleanField(default=False, verbose_name='moderator status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='exists',
            field=models.BooleanField(default=True, verbose_name='Exists'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='questionprogress',
            name='exists',
            field=models.BooleanField(default=True, verbose_name='Exists'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studentexperience',
            name='exists',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studenthistoric',
            name='exists',
            field=models.BooleanField(default=True, verbose_name='Exists'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studentlessonstate',
            name='exists',
            field=models.BooleanField(default=True, verbose_name='Exists'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studentprogress',
            name='exists',
            field=models.BooleanField(default=True, verbose_name='Exists'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videoprogress',
            name='exists',
            field=models.BooleanField(default=True, verbose_name='Exists'),
            preserve_default=True,
        ),
    ]
