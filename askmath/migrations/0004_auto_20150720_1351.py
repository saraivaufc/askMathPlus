# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0003_auto_20150720_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answeredquestionshistoric',
            name='hit',
            field=models.BooleanField(default=False, verbose_name='Hit'),
            preserve_default=True,
        ),
    ]
