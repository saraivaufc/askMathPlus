# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0024_administratorkey_assistantkey_teacherkey'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='administratorkey',
            options={'ordering': ['user'], 'verbose_name': 'Administrator Key', 'verbose_name_plural': 'Administrators Key'},
        ),
        migrations.AlterModelOptions(
            name='assistantkey',
            options={'ordering': ['user'], 'verbose_name': 'Assistant Key', 'verbose_name_plural': 'Assistants Key'},
        ),
        migrations.AlterModelOptions(
            name='teacherkey',
            options={'ordering': ['user'], 'verbose_name': 'Teacher Key', 'verbose_name_plural': 'Teachers Key'},
        ),
    ]
