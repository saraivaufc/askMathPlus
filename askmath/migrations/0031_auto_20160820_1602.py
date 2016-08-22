# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0030_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(default=None, upload_to=b'documents/image/question/%Y/%m/%d', blank=True, help_text='Por favor, entre com uma image.', null=True, verbose_name='Imagem'),
            preserve_default=True,
        ),
    ]
