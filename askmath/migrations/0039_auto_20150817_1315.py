# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0038_auto_20150817_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_image',
            field=models.ImageField(default=None, upload_to='documents/image/profile_image/%Y/%m/%d', blank=True, help_text='Please enter you profile image.', null=True, verbose_name='Profile Image'),
            preserve_default=True,
        ),
    ]
