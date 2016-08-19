# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0015_auto_20160728_0714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='errors_to_obstacle',
            new_name='errors_followed_to_obstacle',
        ),
        migrations.AddField(
            model_name='lesson',
            name='errors_to_deficiency',
            field=models.IntegerField(default=3, help_text='Choose the quantity of errors to deficiency.', verbose_name='Errors to Deficiency'),
            preserve_default=False,
        ),
    ]
