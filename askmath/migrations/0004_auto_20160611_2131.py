# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0003_auto_20160611_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='classes',
            field=models.ManyToManyField(help_text='Choose classe that this student.', related_name='Classes', verbose_name='Classes', to='askmath.Classe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='current_classe',
            field=models.ForeignKey(related_name='Current Classe', default=1, verbose_name='Current Classe', to='askmath.Classe', help_text='Choose the current classe to this student.'),
            preserve_default=False,
        ),
    ]
