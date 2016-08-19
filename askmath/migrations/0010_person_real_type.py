# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('askmath', '0009_remove_person_real_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='real_type',
            field=models.ForeignKey(default=1, editable=False, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
    ]
