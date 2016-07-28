# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0013_student_classes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['first_name'], 'verbose_name': 'Person', 'verbose_name_plural': 'Persons'},
        ),
        migrations.AddField(
            model_name='lesson',
            name='errors_to_obstacle',
            field=models.IntegerField(default=3, help_text='Choose the quantity of errors to obstacle.', verbose_name='Errors to Obstacule'),
            preserve_default=False,
        ),
    ]
