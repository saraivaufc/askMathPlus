# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0030_auto_20150808_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
        migrations.AlterField(
            model_name='contact',
            name='file',
            field=models.FileField(help_text='Perform upload a file.', upload_to=b'documents/contact_files/%Y/%m/%d', null=True, verbose_name='File', blank=True),
            preserve_default=True,
        ),
    ]
