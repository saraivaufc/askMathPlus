# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import askMathPlus.components_metro


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Choose a name for the classe.', max_length=100, verbose_name='Nome')),
                ('semester', models.FloatField(help_text='Choose semester of this classe.', verbose_name='Semester')),
                ('plan', models.FileField(help_text='Realize upload de um arquivo.', upload_to=b'documents/plans/%Y/%m/%d', null=True, verbose_name='Plan', blank=True)),
                ('visible', models.BooleanField(default=False, help_text='Select this option to leave visible classe at all.', verbose_name='Vis\xedvel')),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, help_text='Choose a color for the classe.', max_length=50, verbose_name='Cor', choices=[(b'bg-lime', b'Lime'), (b'bg-green', b'Green'), (b'bg-emerald', b'Emerald'), (b'bg-teal', b'Teal'), (b'bg-blue', b'Blue'), (b'bg-cyan', b'Cyan'), (b'bg-cobalt', b'Cobalt'), (b'bg-indigo', b'Indigo'), (b'bg-violet', b'Violet'), (b'bg-magenta', b'Magenta'), (b'bg-orange', b'Orange'), (b'bg-amber', b'Amber'), (b'bg-yellow', b'Yellow'), (b'bg-brown', b'Brown'), (b'bg-olive', b'Emerald'), (b'bg-steel', b'Steel'), (b'bg-mauve', b'Mauve'), (b'bg-taupe', b'Taupe'), (b'bg-gray', b'Gray'), (b'bg-lightBlue', b'Light Blue'), (b'bg-lightRed', b'Light Red'), (b'bg-lightGreen', b'Light Green'), (b'bg-lighterBlue', b'Lighter Blue'), (b'bg-lightOlive', b'Light Olive'), (b'bg-lightOrange', b'Light Orange'), (b'bg-darkBrown', b'Dark Brown'), (b'bg-darkIndigo', b'Dark Indigo'), (b'bg-darkCyan', b'Dark Cyan'), (b'bg-darkCobalt', b'Dark Cobalt'), (b'bg-darkTeal', b'Dark Teal'), (b'bg-darkEmerald', b'Dark Emerald'), (b'bg-darkGreen', b'Dark Green'), (b'bg-darkOrange', b'Dark Orange'), (b'bg-darkViolet', b'Dark Violet'), (b'bg-darkBlue', b'Dark Blue')])),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
                ('responsible', models.ForeignKey(related_name='Responsible', blank=True, to='askmath.Teacher', help_text='Choose responsible for the classe.', null=True, verbose_name='Respons\xe1vel')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Classe',
                'verbose_name_plural': 'Classes',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='discipline',
            name='responsible',
        ),
        migrations.AddField(
            model_name='discipline',
            name='classe',
            field=models.ForeignKey(blank=True, to='askmath.Classe', help_text='Choose the classe which is discipline belongs.', null=True, verbose_name='Classe'),
            preserve_default=True,
        ),
    ]
