# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0012_auto_20160612_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='classes',
            field=models.ManyToManyField(related_name='Classes', to='askmath.Classe', blank=True, help_text='Choose classe that this student.', null=True, verbose_name='Classes'),
            preserve_default=True,
        ),
    ]
