# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
import askmath.models.access.registerkey
from django.conf import settings
import askMathPlus.components_metro


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministratorKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=askmath.models.access.registerkey.generate_key, max_length=100, verbose_name='Chave')),
                ('in_use', models.BooleanField(default=False, verbose_name='Em Uso')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
            ],
            options={
                'ordering': ['user'],
                'verbose_name': 'Chave do Administrador',
                'verbose_name_plural': 'Chaves dos Administradores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnsweredQuestionsHistoric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hit', models.BooleanField(default=False, verbose_name='Acerto')),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Hist\xf3rico da Quest\xe3o Resolvida',
                'verbose_name_plural': 'Hist\xf3rico de Quest\xf5es Resolvidas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AssistantKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=askmath.models.access.registerkey.generate_key, max_length=100, verbose_name='Chave')),
                ('in_use', models.BooleanField(default=False, verbose_name='Em Uso')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
            ],
            options={
                'ordering': ['user'],
                'verbose_name': 'Chave do Assistente',
                'verbose_name_plural': 'Chave do Assistente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Escolha um t\xedtulo para a categoria.', max_length=100, verbose_name='T\xedtulo')),
                ('description', models.TextField(help_text='Escolha uma descri\xe7\xe3o para a categoria.', max_length=100, null=True, verbose_name='Descri\xe7\xe3o', blank=True)),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, help_text='Escolha uma cor para a categoria.', max_length=50, verbose_name='Cor', choices=[(b'bg-lime', b'Lime'), (b'bg-green', b'Green'), (b'bg-emerald', b'Emerald'), (b'bg-teal', b'Teal'), (b'bg-blue', b'Blue'), (b'bg-cyan', b'Cyan'), (b'bg-cobalt', b'Cobalt'), (b'bg-indigo', b'Indigo'), (b'bg-violet', b'Violet'), (b'bg-magenta', b'Magenta'), (b'bg-orange', b'Orange'), (b'bg-amber', b'Amber'), (b'bg-yellow', b'Yellow'), (b'bg-brown', b'Brown'), (b'bg-olive', b'Emerald'), (b'bg-steel', b'Steel'), (b'bg-mauve', b'Mauve'), (b'bg-taupe', b'Taupe'), (b'bg-gray', b'Gray'), (b'bg-lightBlue', b'Light Blue'), (b'bg-lightRed', b'Light Red'), (b'bg-lightGreen', b'Light Green'), (b'bg-lighterBlue', b'Lighter Blue'), (b'bg-lightOlive', b'Light Olive'), (b'bg-lightOrange', b'Light Orange')])),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(verbose_name='Comment')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['creation'],
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Escolha uma t\xedtulo para a disciplina.', max_length=100, verbose_name='T\xedtulo')),
                ('visible', models.BooleanField(default=False, help_text='Selecione esta op\xe7\xe3o para tornas a disciplina vis\xedvel \xe0 todos.', verbose_name='Vis\xedvel')),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, help_text='Escolha uma cor para a disciplina.', max_length=50, verbose_name='Cor', choices=[(b'bg-lime', b'Lime'), (b'bg-green', b'Green'), (b'bg-emerald', b'Emerald'), (b'bg-teal', b'Teal'), (b'bg-blue', b'Blue'), (b'bg-cyan', b'Cyan'), (b'bg-cobalt', b'Cobalt'), (b'bg-indigo', b'Indigo'), (b'bg-violet', b'Violet'), (b'bg-magenta', b'Magenta'), (b'bg-orange', b'Orange'), (b'bg-amber', b'Amber'), (b'bg-yellow', b'Yellow'), (b'bg-brown', b'Brown'), (b'bg-olive', b'Emerald'), (b'bg-steel', b'Steel'), (b'bg-mauve', b'Mauve'), (b'bg-taupe', b'Taupe'), (b'bg-gray', b'Gray'), (b'bg-lightBlue', b'Light Blue'), (b'bg-lightRed', b'Light Red'), (b'bg-lightGreen', b'Light Green'), (b'bg-lighterBlue', b'Lighter Blue'), (b'bg-lightOlive', b'Light Olive'), (b'bg-lightOrange', b'Light Orange')])),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HelpQuestionsHistoric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('discipline', models.ForeignKey(verbose_name='Disciplina', to='askmath.Discipline')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Hist\xf3rico do Pedido de Ajuda',
                'verbose_name_plural': 'Hist\xf3rico de Pedidos de Ajuda',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(help_text='Escolha uma posi\xe7\xe3o para este item.', null=True, verbose_name='Posi\xe7\xe3o', blank=True)),
                ('description', models.TextField(help_text='Escolha uma descri\xe7\xe3o para este item.', verbose_name='Descri\xe7\xe3o')),
                ('correct', models.BooleanField(default=False, help_text='Este item est\xe1 correto.', verbose_name='\xc9 correta')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'Item',
                'verbose_name_plural': 'Itens',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Escolha uma t\xedtulo para a li\xe7\xe3o.', max_length=50, verbose_name='T\xedtulo')),
                ('description', models.TextField(help_text='Escolha uma descri\xe7\xe3o para a li\xe7\xe3o.', verbose_name='Descri\xe7\xe3o')),
                ('maximum_hops', models.IntegerField(help_text='Escolha o n\xfamero m\xe1ximo de saltos que o aluno pode realizar nessa li\xe7\xe3o.', verbose_name='M\xe1ximo de Saltos')),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, help_text='Escolha uma cor para esta li\xe7\xe3o.', max_length=50, verbose_name='Cor', choices=[(b'bg-lime', b'Lime'), (b'bg-green', b'Green'), (b'bg-emerald', b'Emerald'), (b'bg-teal', b'Teal'), (b'bg-blue', b'Blue'), (b'bg-cyan', b'Cyan'), (b'bg-cobalt', b'Cobalt'), (b'bg-indigo', b'Indigo'), (b'bg-violet', b'Violet'), (b'bg-magenta', b'Magenta'), (b'bg-orange', b'Orange'), (b'bg-amber', b'Amber'), (b'bg-yellow', b'Yellow'), (b'bg-brown', b'Brown'), (b'bg-olive', b'Emerald'), (b'bg-steel', b'Steel'), (b'bg-mauve', b'Mauve'), (b'bg-taupe', b'Taupe'), (b'bg-gray', b'Gray'), (b'bg-lightBlue', b'Light Blue'), (b'bg-lightRed', b'Light Red'), (b'bg-lightGreen', b'Light Green'), (b'bg-lighterBlue', b'Lighter Blue'), (b'bg-lightOlive', b'Light Olive'), (b'bg-lightOrange', b'Light Orange')])),
                ('visible', models.BooleanField(default=False, help_text='Escolha esta op\xe7\xe3o para tornar a li\xe7\xe3o vis\xedvel \xe0 todos.')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('exists', models.BooleanField(default=True)),
                ('discipline', models.ForeignKey(verbose_name='Disciplina', to='askmath.Discipline', help_text='Escolha uma disciplina para a li\xe7\xe3o.')),
                ('requirements', models.ManyToManyField(related_name='Requirements', to='askmath.Lesson', blank=True, help_text='Escolha as li\xe7\xe3o que s\xe3o recomendadas seguir antes de iniciar esta.', null=True, verbose_name='Requisitos')),
                ('sugestions', models.ManyToManyField(related_name='Sugestions', to='askmath.Lesson', blank=True, help_text='Escolha as li\xe7\xe3o que s\xe3o recomendadas seguir ap\xf3s a conclus\xe3o desta.', null=True, verbose_name='Sugest\xf5es')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
            ],
            options={
                'ordering': ['creation'],
                'verbose_name': 'Curtir',
                'verbose_name_plural': 'Curtis',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Entre com seu nome.', max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(help_text='Entre com seu email.', max_length=254, verbose_name='Email')),
                ('message', models.TextField(help_text='Voc\xea pode usar as tags HTML: <a href=\'\' title=\'\'> <abbr title = ""> <acronym title = ""> <b> <blockquote citar = ""> <cite> <code> <del datetime = \'\'> <em> <i> <q cite = ""> <strike> <strong>', max_length=2000, verbose_name='Mensagem')),
                ('file', models.FileField(help_text='Realize upload de um arquivo.', upload_to=b'documents/contact_files/%Y/%m/%d', null=True, verbose_name='Arquivo', blank=True)),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, max_length=50, verbose_name='Cor')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Cria\xe7\xe3o')),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
            ],
            options={
                'ordering': ['creation'],
                'verbose_name': 'Mensagem',
                'verbose_name_plural': 'Mensagens',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_image', models.ImageField(default=None, upload_to='documents/image/profile_image/%Y/%m/%d', blank=True, help_text='Please enter you profile image.', null=True, verbose_name='Profile Image')),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, max_length=50, verbose_name='Color')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-date_joined'],
                'abstract': False,
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='askmath.Person')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Assistant',
                'verbose_name_plural': 'Assistants',
            },
            bases=('askmath.person',),
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='askmath.Person')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Administrator',
                'verbose_name_plural': 'Administrators',
            },
            bases=('askmath.person',),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(help_text='Escolha uma posi\xe7\xe3o para esta pergunta.', verbose_name='Posi\xe7\xe3o')),
                ('description', models.TextField(help_text='Escolha uma descri\xe7\xe3o para esta pergunta.', verbose_name='Descri\xe7\xe3o')),
                ('help', models.TextField(help_text='Escolha uma ajuda para esta pergunta.', null=True, verbose_name='Ajuda', blank=True)),
                ('scores', models.IntegerField(verbose_name='Pontos', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')])),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, help_text='Escolha uma cor para esta quest\xe3o.', max_length=50, verbose_name='Cor', choices=[(b'bg-lime', b'Lime'), (b'bg-green', b'Green'), (b'bg-emerald', b'Emerald'), (b'bg-teal', b'Teal'), (b'bg-blue', b'Blue'), (b'bg-cyan', b'Cyan'), (b'bg-cobalt', b'Cobalt'), (b'bg-indigo', b'Indigo'), (b'bg-violet', b'Violet'), (b'bg-magenta', b'Magenta'), (b'bg-orange', b'Orange'), (b'bg-amber', b'Amber'), (b'bg-yellow', b'Yellow'), (b'bg-brown', b'Brown'), (b'bg-olive', b'Emerald'), (b'bg-steel', b'Steel'), (b'bg-mauve', b'Mauve'), (b'bg-taupe', b'Taupe'), (b'bg-gray', b'Gray'), (b'bg-lightBlue', b'Light Blue'), (b'bg-lightRed', b'Light Red'), (b'bg-lightGreen', b'Light Green'), (b'bg-lighterBlue', b'Lighter Blue'), (b'bg-lightOlive', b'Light Olive'), (b'bg-lightOrange', b'Light Orange')])),
                ('visible', models.BooleanField(default=False, help_text='Selecione esta op\xe7\xe3o para tornar esta quest\xe3o vis\xedvel \xe0 todos.', verbose_name='Vis\xedvel')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
                ('items', models.ManyToManyField(help_text='Escolha os itens que esta pergunta tem.', to='askmath.Item', verbose_name='Itens')),
                ('lesson', models.ForeignKey(verbose_name='Li\xe7\xe3o', to='askmath.Lesson', help_text='Escolha uma li\xe7\xe3o para esta pergunta.')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'Quest\xe3o',
                'verbose_name_plural': 'Quest\xf5es',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkippedQuestionsHistoric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('discipline', models.ForeignKey(verbose_name='Disciplina', to='askmath.Discipline')),
                ('lesson', models.ForeignKey(verbose_name='Li\xe7\xe3o', to='askmath.Lesson')),
                ('question', models.ForeignKey(verbose_name='Quest\xe3o', to='askmath.Question')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Hist\xf3rico o Salto Realizado',
                'verbose_name_plural': 'Hist\xf3rico de Saltos Realizados',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='askmath.Person')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
            bases=('askmath.person',),
        ),
        migrations.CreateModel(
            name='StudentExperience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scores', models.IntegerField(default=0, verbose_name='Pontos')),
                ('max_scores', models.IntegerField(default=10, verbose_name='M\xe1ximo de Pontos')),
                ('level', models.IntegerField(default=1, verbose_name='N\xedvel')),
                ('stars', models.IntegerField(default=0, verbose_name='Estrelas')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('exists', models.BooleanField(default=True)),
                ('student', models.ForeignKey(verbose_name='Estudante', to='askmath.Student')),
            ],
            options={
                'ordering': ['-student'],
                'verbose_name': 'Experi\xeancia do Estudante',
                'verbose_name_plural': 'Experi\xeancias dos Estudantes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentHistoric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('answered_questions_historic', models.ManyToManyField(related_name='Hist\xf3rico de Quest\xf5es Resolvidas', null=True, verbose_name='Hist\xf3rico de Quest\xf5es Resolvidas', to='askmath.AnsweredQuestionsHistoric', blank=True)),
                ('help_questions_historic', models.ManyToManyField(related_name='Help Question Historic', null=True, verbose_name='Hist\xf3rico de Quest\xf5es Resolvidas', to='askmath.HelpQuestionsHistoric', blank=True)),
                ('skipped_questions_historic', models.ManyToManyField(related_name='Skipped Question Historic', null=True, verbose_name='Hist\xf3rico de Quest\xf5es Resolvidas', to='askmath.SkippedQuestionsHistoric', blank=True)),
                ('student', models.ForeignKey(verbose_name='Estudante', to='askmath.Student')),
            ],
            options={
                'ordering': ['-student'],
                'verbose_name': 'Hist\xf3rico de Estudante',
                'verbose_name_plural': 'Hist\xf3rico de Estudantes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentLessonState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scores', models.IntegerField(default=0, verbose_name='Pontos')),
                ('remaining_jump', models.IntegerField(default=0, verbose_name='Saltos Restantes')),
                ('hits_followed', models.IntegerField(default=0, verbose_name='Acertos Seguidos')),
                ('errors_followed', models.IntegerField(default=0, verbose_name='Erros Seguidos')),
                ('percentage_completed', models.IntegerField(default=0, verbose_name='Porcentagem Completo')),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('answered_correct_questions', models.ManyToManyField(related_name='Answered Correct Questions', null=True, verbose_name='Quest\xf5es Respondidas', to='askmath.Question', blank=True)),
                ('answered_incorrect_questions', models.ManyToManyField(related_name='Answered Incorrect Questions', null=True, verbose_name='Quest\xf5es Respondidas', to='askmath.Question', blank=True)),
                ('discipline', models.ForeignKey(verbose_name='Disciplina', to='askmath.Discipline')),
                ('help_questions', models.ManyToManyField(related_name='Help Questions', null=True, verbose_name='Quest\xf5es de Ajuda', to='askmath.Question', blank=True)),
                ('lesson', models.ForeignKey(verbose_name='Li\xe7\xe3o', to='askmath.Lesson')),
                ('skipped_questions', models.ManyToManyField(related_name='Skipped Questions', null=True, verbose_name='Quest\xf5es Saltadas', to='askmath.Question', blank=True)),
                ('student', models.ForeignKey(verbose_name='Estudante', to='askmath.Student')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Estado do Estudante nas Li\xe7\xf5es',
                'verbose_name_plural': 'Estado das Li\xe7\xf5es dos Estudantes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentQuestionProgress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('discipline', models.ForeignKey(verbose_name='Disciplina', to='askmath.Discipline')),
                ('lesson', models.ForeignKey(verbose_name='Li\xe7\xe3o', to='askmath.Lesson')),
                ('question', models.ForeignKey(verbose_name='Quest\xe3o', to='askmath.Question')),
                ('student', models.ForeignKey(verbose_name='Estudante', to='askmath.Student')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Progresso da Quest\xe3o',
                'verbose_name_plural': 'Progresso das Quest\xf5es',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentVideoProgress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('discipline', models.ForeignKey(verbose_name='Disciplina', to='askmath.Discipline')),
                ('lesson', models.ForeignKey(verbose_name='Li\xe7\xe3o', to='askmath.Lesson')),
                ('student', models.ForeignKey(verbose_name='Estudante', to='askmath.Student')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Progresso do V\xeddeo',
                'verbose_name_plural': 'Progresso do V\xeddeo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='askmath.Person')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
            bases=('askmath.person',),
        ),
        migrations.CreateModel(
            name='TeacherKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=askmath.models.access.registerkey.generate_key, max_length=100, verbose_name='Chave')),
                ('in_use', models.BooleanField(default=False, verbose_name='Em Uso')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
                ('creator', models.ForeignKey(verbose_name='Pessoa', to='askmath.Person')),
                ('user', models.ForeignKey(related_name='Teacher', blank=True, to='askmath.Teacher', null=True)),
            ],
            options={
                'ordering': ['user'],
                'verbose_name': 'Chave do Professor',
                'verbose_name_plural': 'Chaves dos Professores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='T\xedtulo')),
                ('description', models.TextField(help_text='Escolha uma descri\xe7\xe3o para esse t\xf3pico.', verbose_name='Descri\xe7\xe3o')),
                ('file', models.FileField(help_text='Realize upload de um arquivo.', upload_to=b'documents/forum/topic/%Y/%m/%d', null=True, verbose_name='Arquivo', blank=True)),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, help_text='Escolha uma cor para este t\xf3pico.', max_length=50, verbose_name='Cor', choices=[(b'bg-lime', b'Lime'), (b'bg-green', b'Green'), (b'bg-emerald', b'Emerald'), (b'bg-teal', b'Teal'), (b'bg-blue', b'Blue'), (b'bg-cyan', b'Cyan'), (b'bg-cobalt', b'Cobalt'), (b'bg-indigo', b'Indigo'), (b'bg-violet', b'Violet'), (b'bg-magenta', b'Magenta'), (b'bg-orange', b'Orange'), (b'bg-amber', b'Amber'), (b'bg-yellow', b'Yellow'), (b'bg-brown', b'Brown'), (b'bg-olive', b'Emerald'), (b'bg-steel', b'Steel'), (b'bg-mauve', b'Mauve'), (b'bg-taupe', b'Taupe'), (b'bg-gray', b'Gray'), (b'bg-lightBlue', b'Light Blue'), (b'bg-lightRed', b'Light Red'), (b'bg-lightGreen', b'Light Green'), (b'bg-lighterBlue', b'Lighter Blue'), (b'bg-lightOlive', b'Light Olive'), (b'bg-lightOrange', b'Light Orange')])),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
                ('category', models.ForeignKey(verbose_name='Categoria', to='askmath.Category')),
                ('likes', models.ManyToManyField(to='askmath.Like', null=True, verbose_name='Curtis', blank=True)),
                ('person', models.ForeignKey(verbose_name='Pessoa', to='askmath.Person')),
            ],
            options={
                'ordering': ['-creation'],
                'verbose_name': 'T\xf3pico',
                'verbose_name_plural': 'T\xf3picos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(help_text='Escolha uma posi\xe7\xe3o para o v\xeddeo.', null=True, verbose_name='Posi\xe7\xe3o', blank=True)),
                ('title', models.CharField(help_text='Escolha um t\xedtulo para o v\xeddeo.', max_length=50, verbose_name='T\xedtulo')),
                ('description', models.TextField(help_text='Escolha uma descri\xe7\xe3o para o v\xeddeo.', null=True, verbose_name='Descri\xe7\xe3o', blank=True)),
                ('file', models.FileField(help_text='Realize upload de um arquivo.', upload_to=b'documents/video/%Y/%m/%d', verbose_name='Arquivo')),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, help_text='Escolha uma cor para o v\xeddeo.', max_length=50, verbose_name='Cor', choices=[(b'bg-lime', b'Lime'), (b'bg-green', b'Green'), (b'bg-emerald', b'Emerald'), (b'bg-teal', b'Teal'), (b'bg-blue', b'Blue'), (b'bg-cyan', b'Cyan'), (b'bg-cobalt', b'Cobalt'), (b'bg-indigo', b'Indigo'), (b'bg-violet', b'Violet'), (b'bg-magenta', b'Magenta'), (b'bg-orange', b'Orange'), (b'bg-amber', b'Amber'), (b'bg-yellow', b'Yellow'), (b'bg-brown', b'Brown'), (b'bg-olive', b'Emerald'), (b'bg-steel', b'Steel'), (b'bg-mauve', b'Mauve'), (b'bg-taupe', b'Taupe'), (b'bg-gray', b'Gray'), (b'bg-lightBlue', b'Light Blue'), (b'bg-lightRed', b'Light Red'), (b'bg-lightGreen', b'Light Green'), (b'bg-lighterBlue', b'Lighter Blue'), (b'bg-lightOlive', b'Light Olive'), (b'bg-lightOrange', b'Light Orange')])),
                ('visible', models.BooleanField(default=False, help_text='Selecione esta op\xe7\xe3o para tornar esse v\xeddeo vis\xedvel \xe0 todos.', verbose_name='Vis\xedvel')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o')),
                ('exists', models.BooleanField(default=True, verbose_name='Existe')),
                ('lesson', models.ForeignKey(verbose_name='Li\xe7\xe3o', to='askmath.Lesson', help_text='Escolha uma li\xe7\xe3o para o v\xeddeo.')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'V\xeddeo',
                'verbose_name_plural': 'V\xeddeos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='studentvideoprogress',
            name='video',
            field=models.ForeignKey(verbose_name='V\xeddeo', to='askmath.Video'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='like',
            name='person',
            field=models.ForeignKey(verbose_name='Pessoa', to='askmath.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='deficiencys',
            field=models.ManyToManyField(help_text='Escolha as poss\xedveis defici\xeancias que o aluno possa ter caso o mesmo responda mancando este item.', to='askmath.Lesson', null=True, verbose_name='Defici\xeancias', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpquestionshistoric',
            name='lesson',
            field=models.ForeignKey(verbose_name='Li\xe7\xe3o', to='askmath.Lesson'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpquestionshistoric',
            name='question',
            field=models.ForeignKey(verbose_name='Quest\xe3o', to='askmath.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discipline',
            name='responsible',
            field=models.ForeignKey(related_name='Responsible', blank=True, to='askmath.Teacher', help_text='Escolha uma respons\xe1vel para a disciplina.', null=True, verbose_name='Respons\xe1vel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(to='askmath.Like', null=True, verbose_name='Likes', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='person',
            field=models.ForeignKey(verbose_name='Person', to='askmath.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(verbose_name='Topic', to='askmath.Topic'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='person',
            field=models.ForeignKey(verbose_name='Pessoa', to='askmath.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assistantkey',
            name='creator',
            field=models.ForeignKey(verbose_name='Pessoa', to='askmath.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assistantkey',
            name='user',
            field=models.ForeignKey(related_name='Assistant', blank=True, to='askmath.Assistant', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answeredquestionshistoric',
            name='discipline',
            field=models.ForeignKey(verbose_name='Disciplina', to='askmath.Discipline'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answeredquestionshistoric',
            name='items',
            field=models.ManyToManyField(to='askmath.Item', verbose_name='Itens'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answeredquestionshistoric',
            name='lesson',
            field=models.ForeignKey(verbose_name='Li\xe7\xe3o', to='askmath.Lesson'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answeredquestionshistoric',
            name='question',
            field=models.ForeignKey(verbose_name='Quest\xe3o', to='askmath.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='administratorkey',
            name='creator',
            field=models.ForeignKey(verbose_name='Pessoa', to='askmath.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='administratorkey',
            name='user',
            field=models.ForeignKey(related_name='Administrator', blank=True, to='askmath.Administrator', null=True),
            preserve_default=True,
        ),
    ]
