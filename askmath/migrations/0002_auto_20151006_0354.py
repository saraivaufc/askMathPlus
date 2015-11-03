# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import askMathPlus.components_metro


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Enter yout name.', max_length=100, verbose_name='Name')),
                ('email', models.EmailField(help_text='Enter yout email.', max_length=254, verbose_name='Email')),
                ('message', models.TextField(help_text='Your use here tags HTML: <a href= title=> <abbr title=> <acronym title=> <b> <blockquote cite=> <cite> <code> <del datetime=> <em> <i> <q cite=> <strike> <strong> ', max_length=2000, verbose_name='Message')),
                ('file', models.FileField(help_text='Perform upload a file.', upload_to=b'documents/contact_files/%Y/%m/%d', null=True, verbose_name='Ficheiro', blank=True)),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, max_length=50, verbose_name='Color')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['creation'],
                'verbose_name': 'Message',
                'verbose_name_plural': 'Mensagens',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AlterField(
            model_name='topic',
            name='file',
            field=models.FileField(help_text='Perform upload a file.', upload_to=b'documents/forum/topic/%Y/%m/%d', null=True, verbose_name='Ficheiro', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(help_text='Perform upload a file.', upload_to=b'documents/video/%Y/%m/%d', verbose_name='Ficheiro'),
            preserve_default=True,
        ),
    ]
