# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0020_auto_20160806_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentexperience',
            name='round',
        ),
    ]