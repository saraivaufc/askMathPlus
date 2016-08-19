# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0014_auto_20160728_0624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='deficiencys',
            new_name='deficiencies',
        ),
    ]
