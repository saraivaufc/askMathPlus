# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0028_auto_20160811_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(default=None, upload_to=b'documents/image/question/%Y/%m/%d', blank=True, help_text='Please enter  image.', null=True, verbose_name='Imagem'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='help',
            field=models.TextField(help_text='Escolha uma ajuda para esta pergunta.', null=True, verbose_name='Ajuda', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentexperience',
            name='date_end_new_round',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de t\xe9rmino da Rodada'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentexperience',
            name='date_start_new_round',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de in\xedcio da Rodada'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentexperience',
            name='full_scores',
            field=models.IntegerField(default=0, verbose_name='Todos os Pontos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentexperience',
            name='last_new_scores',
            field=models.IntegerField(default=0, verbose_name='\xdaltimos pontos ganhos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentexperience',
            name='last_scores',
            field=models.IntegerField(default=0, verbose_name='\xdaltimos Pontos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentexperience',
            name='new_scores',
            field=models.IntegerField(default=0, verbose_name='Novos Pontos'),
            preserve_default=True,
        ),
    ]
