# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0011_remove_person_real_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='classes',
        ),
        migrations.AddField(
            model_name='classe',
            name='students',
            field=models.ManyToManyField(help_text='Choose students that this classe.', to='askmath.Student', null=True, verbose_name='Estudantes', blank=True),
            preserve_default=True,
        ),
    ]
