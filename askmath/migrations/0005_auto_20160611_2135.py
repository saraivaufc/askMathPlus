# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0004_auto_20160611_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='classes',
            field=models.ManyToManyField(related_name='Classes', to='askmath.Classe', blank=True, help_text='Choose classe that this student.', null=True, verbose_name='Classes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='current_classe',
            field=models.ForeignKey(related_name='Current Classe', blank=True, to='askmath.Classe', help_text='Choose the current classe to this student.', null=True, verbose_name='Current Classe'),
            preserve_default=True,
        ),
    ]
