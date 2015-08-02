# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import re
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('location', models.CharField(max_length=75, null=True, verbose_name='location', blank=True)),
                ('last_seen', models.DateTimeField(auto_now=True, verbose_name='last seen')),
                ('last_ip', models.GenericIPAddressField(null=True, verbose_name='last ip', blank=True)),
                ('is_administrator', models.BooleanField(default=False, verbose_name='administrator status')),
                ('is_moderator', models.BooleanField(default=False, verbose_name='moderator status')),
                ('username', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Enter a valid username.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters', unique=True, verbose_name='username', db_index=True)),
                ('firstname', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('lastname', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='email')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_image', models.ImageField(default=None, upload_to='documents/image/profile_image/%Y/%m/%d', null=True, verbose_name='Profile Image', blank=True)),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-date_joined'],
                'abstract': False,
                'verbose_name_plural': 'persons',
                'db_table': 'auth_user',
                'verbose_name': 'person',
                'swappable': 'AUTH_USER_MODEL',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'administrator',
                'verbose_name_plural': 'administrators',
            },
            bases=('askmath.person',),
        ),
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'assistant',
                'verbose_name_plural': 'assistants',
            },
            bases=('askmath.person',),
        ),
        migrations.CreateModel(
            name='IDiscipline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('idiscipline_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='askmath.IDiscipline')),
                ('title', models.CharField(help_text='Choose a title for the discipline.', max_length=100, verbose_name='Title')),
                ('responsible', models.CharField(help_text='Choose responsible for the discipline.', max_length=100, null=True, verbose_name='Responsible', blank=True)),
                ('visible', models.BooleanField(default=False, help_text='Select this option to leave visible discipline at all.', verbose_name='Visible')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['-title'],
                'verbose_name': 'Discipline',
                'verbose_name_plural': 'Disciplines',
            },
            bases=('askmath.idiscipline',),
        ),
        migrations.CreateModel(
            name='IItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ILesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('iitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='askmath.IItem')),
                ('position', models.IntegerField(help_text='Choose the position which is item belongs.', null=True, verbose_name='Position', blank=True)),
                ('description', models.TextField(help_text='Choose a description for item is.', verbose_name='Description')),
                ('is_correct', models.BooleanField(default=False, help_text='Say if this item is correct.', verbose_name='Is Correct')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
            bases=('askmath.iitem',),
        ),
        migrations.CreateModel(
            name='IVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('ilesson_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='askmath.ILesson')),
                ('title', models.CharField(help_text='Choose a title for lesson is.', max_length=50, verbose_name='Title')),
                ('description', models.TextField(help_text='Choose a description for lesson is.', verbose_name='Description')),
                ('maximum_hops', models.IntegerField(help_text='Choose the maximum number of hops that the student can perform this lesson.', verbose_name='Maximum Hops')),
                ('visible', models.BooleanField(default=False, help_text='Select this option to leave visible lesson at all.')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True)),
                ('disciplines', models.ManyToManyField(help_text='Choose the disciplines which is lesson belongs.', to='askmath.Discipline', null=True, verbose_name='Disciplines', blank=True)),
                ('requirements', models.ManyToManyField(related_name='Requirements', to='askmath.Lesson', blank=True, help_text='Choose the lessons is recommended completion before continuing this.', null=True, verbose_name='Requirements')),
                ('sugestions', models.ManyToManyField(related_name='Sugestions', to='askmath.Lesson', blank=True, help_text='Choose the lessons is recommended pursue after completing this.', null=True, verbose_name='Sugestions')),
            ],
            options={
                'ordering': ['-title'],
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
            bases=('askmath.ilesson',),
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'permissions': (('access_manager', 'Access Manager'), ('access_manager_person', 'Access Manager Person'), ('read_person', 'Read Person'), ('write_person', 'Write Person'), ('access_manager_student_historic', 'Access Manager Student Historic'), ('read_student_historic', 'Read StudentHistoric'), ('write_student_historic', 'Write StudentHistoric'), ('access_manager_student_progress', 'Access Manager Student Progress'), ('read_student_progress', 'Read StudentProgress'), ('write_student_progress', 'Write StudentProgress'), ('access_manager_student_state', 'Access Manager Student State'), ('read_student_state', 'Read StudentState'), ('write_student_state', 'Write StudentState'), ('access_manager_student_statistics', 'Access Manager Student Statistics'), ('read_student_statistics', 'Read StudentStatistics'), ('write_student_statistics', 'Write StudentStatistics'), ('access_manager_discipline', 'Access Manager Discipline'), ('read_discipline', 'Read Discipline'), ('write_discipline', 'Write Discipline'), ('access_manager_lesson', 'Access Manager Lesson'), ('read_lesson', 'Read Lesson'), ('write_lesson', 'Write Lesson'), ('access_manager_question', 'Access Manager Question'), ('read_question', 'Read Question'), ('write_question', 'Write Question'), ('access_manager_video', 'Access Manager Video'), ('read_video', 'Read Video'), ('write_video', 'Write Video')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('iquestion_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='askmath.IQuestion')),
                ('position', models.IntegerField(help_text='Choose the position which is question belongs.', null=True, verbose_name='Position', blank=True)),
                ('description', models.TextField(help_text='Choose a description for question is.', verbose_name='Description')),
                ('help', models.TextField(help_text='Choose a help to this question.', null=True, verbose_name='Help', blank=True)),
                ('scores', models.IntegerField(verbose_name='Scores')),
                ('visible', models.BooleanField(default=False, help_text='Select this option to leave visible question at all.', verbose_name='Visible')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('items', models.ManyToManyField(help_text='Choose items that this issue has.', to='askmath.Item', verbose_name='Items')),
                ('lesson', models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson', help_text='Choose the lesson which is question belongs.')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
            bases=('askmath.iquestion',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
            },
            bases=('askmath.person',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'teacher',
                'verbose_name_plural': 'teachers',
            },
            bases=('askmath.person',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('ivideo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='askmath.IVideo')),
                ('position', models.IntegerField(help_text='Choose the position which is video belongs.', null=True, verbose_name='Position', blank=True)),
                ('title', models.CharField(help_text='Choose a title for video is.', max_length=50, verbose_name='Title')),
                ('description', models.TextField(help_text='Choose a description for video is.', null=True, verbose_name='Description', blank=True)),
                ('video', models.FileField(help_text='Perform upload a video.', upload_to=b'documents/video/%Y/%m/%d', verbose_name='Video')),
                ('visible', models.BooleanField(default=False, help_text='Select this option to leave visible video at all.', verbose_name='Visible')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('lesson', models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson', help_text='Choose the lesson which is video belongs.')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
            bases=('askmath.ivideo',),
        ),
        migrations.AddField(
            model_name='item',
            name='deficiencys',
            field=models.ManyToManyField(help_text='Choose possible deficiencies that the student may have if he opts for this item.', to='askmath.Lesson', null=True, verbose_name='Deficiencys', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
