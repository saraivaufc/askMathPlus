# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administratorkey',
            name='creator',
            field=models.ForeignKey(verbose_name='Usu\xe1rio', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assistantkey',
            name='creator',
            field=models.ForeignKey(verbose_name='Usu\xe1rio', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacherkey',
            name='creator',
            field=models.ForeignKey(verbose_name='Usu\xe1rio', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
