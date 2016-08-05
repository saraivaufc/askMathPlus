# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import askMathPlus.components_metro


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0016_auto_20160728_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='color',
            field=models.CharField(default=askMathPlus.components_metro.generate_color, help_text='Escolha uma cor para esta turma.', max_length=50, verbose_name='Cor', choices=[(b'bg-lime', b'Lime'), (b'bg-green', b'Green'), (b'bg-emerald', b'Emerald'), (b'bg-teal', b'Teal'), (b'bg-blue', b'Blue'), (b'bg-cyan', b'Cyan'), (b'bg-cobalt', b'Cobalt'), (b'bg-indigo', b'Indigo'), (b'bg-violet', b'Violet'), (b'bg-magenta', b'Magenta'), (b'bg-orange', b'Orange'), (b'bg-amber', b'Amber'), (b'bg-yellow', b'Yellow'), (b'bg-brown', b'Brown'), (b'bg-olive', b'Emerald'), (b'bg-steel', b'Steel'), (b'bg-mauve', b'Mauve'), (b'bg-taupe', b'Taupe'), (b'bg-gray', b'Gray'), (b'bg-lightBlue', b'Light Blue'), (b'bg-lightRed', b'Light Red'), (b'bg-lightGreen', b'Light Green'), (b'bg-lighterBlue', b'Lighter Blue'), (b'bg-lightOlive', b'Light Olive'), (b'bg-lightOrange', b'Light Orange'), (b'bg-darkBrown', b'Dark Brown'), (b'bg-darkIndigo', b'Dark Indigo'), (b'bg-darkCyan', b'Dark Cyan'), (b'bg-darkCobalt', b'Dark Cobalt'), (b'bg-darkTeal', b'Dark Teal'), (b'bg-darkEmerald', b'Dark Emerald'), (b'bg-darkGreen', b'Dark Green'), (b'bg-darkOrange', b'Dark Orange'), (b'bg-darkViolet', b'Dark Violet'), (b'bg-darkBlue', b'Dark Blue')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classe',
            name='disciplines',
            field=models.ManyToManyField(help_text='Escolha as disciplinas que esta turma ter\xe1.', to='askmath.Discipline', null=True, verbose_name='Disciplinas', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classe',
            name='name',
            field=models.CharField(help_text='Escolha um nome para a turma.', max_length=100, verbose_name='Nome'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classe',
            name='responsible',
            field=models.ForeignKey(related_name='Responsible', blank=True, to='askmath.Teacher', help_text='Escolha uma respons\xe1vel para a turma.', null=True, verbose_name='Respons\xe1vel'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classe',
            name='semester',
            field=models.FloatField(help_text='Escolha o semestre dessa turma.', verbose_name='Semestre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classe',
            name='students',
            field=models.ManyToManyField(help_text='Escolha os estudantes dessa turma.', to='askmath.Student', null=True, verbose_name='Estudantes', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classe',
            name='visible',
            field=models.BooleanField(default=False, help_text='Escolha esta op\xe7\xe3o para tornar a turma vis\xedvel \xe0 todos.', verbose_name='Vis\xedvel'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='errors_followed_to_obstacle',
            field=models.IntegerField(help_text='Escolha a quantidade de erros para o obst\xe1culo.', verbose_name='Erros para Obst\xe1culo.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='errors_to_deficiency',
            field=models.IntegerField(help_text='Escolha a quantidade de erros para o obst\xe1culo.', verbose_name='Erros para a Defici\xeancia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(null=True, max_length=254, blank=True, help_text='Please enter you email.', unique=True, verbose_name='Email'),
            preserve_default=True,
        ),
    ]
