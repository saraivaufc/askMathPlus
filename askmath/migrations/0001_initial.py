# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.timezone
from django.conf import settings
import askmath.models.access.registerkey
import askMathPlus.components_metro


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
                ('username', models.CharField(help_text='Please enter you username.', unique=True, max_length=30, verbose_name='Username', db_index=True)),
                ('name', models.CharField(help_text='Please enter you name.', max_length=100, null=True, verbose_name='Name')),
                ('email', models.EmailField(help_text='Please enter you email.', unique=True, max_length=254, verbose_name='Email')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_image', models.ImageField(default=None, upload_to='documents/image/profile_image/%Y/%m/%d', blank=True, help_text='Please enter you profile image.', null=True, verbose_name='Profile Image')),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, max_length=50, verbose_name='Color')),
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
            name='AdministratorKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=askmath.models.access.registerkey.generate_key, max_length=100, verbose_name='Key *')),
                ('in_use', models.BooleanField(default=False, verbose_name='In Use')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['user'],
                'verbose_name': 'Administrator Key',
                'verbose_name_plural': 'Administrators Key',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnsweredQuestionsHistoric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hit', models.BooleanField(default=False, verbose_name='Hit')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Answered Question Historic',
                'verbose_name_plural': 'Answered Questions Historic',
            },
            bases=(models.Model,),
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
            name='AssistantKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=askmath.models.access.registerkey.generate_key, max_length=100, verbose_name='Key *')),
                ('in_use', models.BooleanField(default=False, verbose_name='In Use')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['user'],
                'verbose_name': 'Assistant Key',
                'verbose_name_plural': 'Assistants Key',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(help_text='Your use here tags HTML: <a href= title=> <abbr title=> <acronym title=> <b> <blockquote cite=> <cite> <code> <del datetime=> <em> <i> <q cite=> <strike> <strong> ', max_length=2000, verbose_name='Message')),
                ('file', models.FileField(help_text='Perform upload a file.', upload_to=b'documents/contact_files/%Y/%m/%d', null=True, verbose_name='File', blank=True)),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, max_length=50, verbose_name='Color')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['creation'],
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Choose a title for the discipline.', max_length=100, verbose_name='Title')),
                ('responsible', models.CharField(help_text='Choose responsible for the discipline.', max_length=100, null=True, verbose_name='Responsible', blank=True)),
                ('visible', models.BooleanField(default=False, help_text='Select this option to leave visible discipline at all.', verbose_name='Visible')),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, max_length=50, verbose_name='Color')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Discipline',
                'verbose_name_plural': 'Disciplines',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HelpQuestionsHistoric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('discipline', models.ForeignKey(verbose_name='Discipline', to='askmath.Discipline')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Help Question Historic',
                'verbose_name_plural': 'Help Questions Historic',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(help_text='Choose the position which is item belongs.', null=True, verbose_name='Position', blank=True)),
                ('description', models.TextField(help_text='Choose a description for item is.', verbose_name='Description')),
                ('correct', models.BooleanField(default=False, help_text='Say if this item is correct.', verbose_name='Is Correct')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Choose a title for lesson is.', max_length=50, verbose_name='Title')),
                ('description', models.TextField(help_text='Choose a description for lesson is.', verbose_name='Description')),
                ('maximum_hops', models.IntegerField(help_text='Choose the maximum number of hops that the student can perform this lesson.', verbose_name='Maximum Hops')),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, max_length=50, verbose_name='Color')),
                ('visible', models.BooleanField(default=False, help_text='Select this option to leave visible lesson at all.')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True)),
                ('disciplines', models.ManyToManyField(help_text='Choose the disciplines which is lesson belongs.', to='askmath.Discipline', verbose_name='Disciplines')),
                ('requirements', models.ManyToManyField(related_name='Requirements', to='askmath.Lesson', blank=True, help_text='Choose the lessons is recommended completion before continuing this.', null=True, verbose_name='Requirements')),
                ('sugestions', models.ManyToManyField(related_name='Sugestions', to='askmath.Lesson', blank=True, help_text='Choose the lessons is recommended pursue after completing this.', null=True, verbose_name='Sugestions')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'permissions': (('access_manager', 'Access Manager'), ('access_content', 'Access Content'), ('access_manager_person', 'Access Manager Person'), ('read_person', 'Read Person'), ('write_person', 'Write Person'), ('write_administrator', 'Write Administrator'), ('write_teacher', 'Write Teacher'), ('write_assistant', 'Write Assistant'), ('write_student', 'Write Student'), ('access_manager_student_historic', 'Access Manager Student Historic'), ('read_student_historic', 'Read StudentHistoric'), ('write_student_historic', 'Write StudentHistoric'), ('access_manager_student_progress', 'Access Manager Student Progress'), ('read_student_progress', 'Read StudentProgress'), ('write_student_progress', 'Write StudentProgress'), ('access_manager_student_state', 'Access Manager Student State'), ('read_student_state', 'Read StudentState'), ('write_student_state', 'Write StudentState'), ('access_manager_statistics', 'Access Manager Statistics'), ('read_statistics', 'Read Statistics'), ('write_statistics', 'Write Statistics'), ('access_manager_discipline', 'Access Manager Discipline'), ('read_discipline', 'Read Discipline'), ('write_discipline', 'Write Discipline'), ('access_manager_lesson', 'Access Manager Lesson'), ('read_lesson', 'Read Lesson'), ('write_lesson', 'Write Lesson'), ('access_manager_question', 'Access Manager Question'), ('read_question', 'Read Question'), ('write_question', 'Write Question'), ('access_manager_video', 'Access Manager Video'), ('read_video', 'Read Video'), ('write_video', 'Write Video'), ('access_manager_contact', 'Access Manager Contact'), ('read_contact', 'Read Contact'), ('write_contact', 'Write Contact')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(help_text='Choose the position which is question belongs.', verbose_name='Position')),
                ('description', models.TextField(help_text='Choose a description for question is.', verbose_name='Description')),
                ('help', models.TextField(help_text='Choose a help to this question.', null=True, verbose_name='Help', blank=True)),
                ('scores', models.IntegerField(verbose_name='Scores', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')])),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, max_length=50, verbose_name='Color')),
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
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkippedQuestionsHistoric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('discipline', models.ForeignKey(verbose_name='Discipline', to='askmath.Discipline')),
                ('lesson', models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson')),
                ('question', models.ForeignKey(verbose_name='Question', to='askmath.Question')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Skipped Question Historic',
                'verbose_name_plural': 'Skipped Questions Historic',
            },
            bases=(models.Model,),
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
            name='StudentExperience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scores', models.IntegerField(default=0, verbose_name='Scores')),
                ('max_scores', models.IntegerField(default=10, verbose_name='Max Scores')),
                ('level', models.IntegerField(default=1, verbose_name='Level')),
                ('stars', models.IntegerField(default=0, verbose_name='Stars')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True)),
                ('student', models.ForeignKey(verbose_name='Student', to='askmath.Student')),
            ],
            options={
                'ordering': ['-student'],
                'verbose_name': 'Student Experience',
                'verbose_name_plural': 'Student Experiences',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentHistoric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('answered_questions_historic', models.ManyToManyField(related_name='Answered Questions Historic', null=True, verbose_name='Answered Questions Historic', to='askmath.AnsweredQuestionsHistoric', blank=True)),
                ('help_questions_historic', models.ManyToManyField(related_name='Help Question Historic', null=True, verbose_name='Answered Questions Historic', to='askmath.HelpQuestionsHistoric', blank=True)),
                ('skipped_questions_historic', models.ManyToManyField(related_name='Skipped Question Historic', null=True, verbose_name='Answered Questions Historic', to='askmath.SkippedQuestionsHistoric', blank=True)),
                ('student', models.ForeignKey(verbose_name='Student', to='askmath.Student')),
            ],
            options={
                'ordering': ['-student'],
                'verbose_name': 'Student Historic',
                'verbose_name_plural': 'Students Historic',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentLessonState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scores', models.IntegerField(default=0, verbose_name='Scores')),
                ('remaining_jump', models.IntegerField(default=0, verbose_name='Remaining Jump')),
                ('hits_followed', models.IntegerField(default=0, verbose_name='Hits Followed')),
                ('errors_followed', models.IntegerField(default=0, verbose_name='Errors Followed')),
                ('percentage_completed', models.IntegerField(default=0, verbose_name='Percentage Completed')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('answered_correct_questions', models.ManyToManyField(related_name='Answered Correct Questions', null=True, verbose_name='Answered Questions', to='askmath.Question', blank=True)),
                ('answered_incorrect_questions', models.ManyToManyField(related_name='Answered Incorrect Questions', null=True, verbose_name='Answered Questions', to='askmath.Question', blank=True)),
                ('discipline', models.ForeignKey(verbose_name='Discipline', to='askmath.Discipline')),
                ('help_questions', models.ManyToManyField(related_name='Help Questions', null=True, verbose_name='Help Questions', to='askmath.Question', blank=True)),
                ('lesson', models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson')),
                ('skipped_questions', models.ManyToManyField(related_name='Skipped Questions', null=True, verbose_name='Skipped Questions', to='askmath.Question', blank=True)),
                ('student', models.ForeignKey(verbose_name='Student', to='askmath.Student')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Student Lesson State',
                'verbose_name_plural': 'Students Lessons State',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentQuestionProgress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('discipline', models.ForeignKey(verbose_name='Discipline', to='askmath.Discipline')),
                ('lesson', models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson')),
                ('question', models.ForeignKey(verbose_name='Question', to='askmath.Question')),
                ('student', models.ForeignKey(verbose_name='Student', to='askmath.Student')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Question Progress',
                'verbose_name_plural': 'Questions Progress',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentVideoProgress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('discipline', models.ForeignKey(verbose_name='Discipline', to='askmath.Discipline')),
                ('lesson', models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson')),
                ('student', models.ForeignKey(verbose_name='Student', to='askmath.Student')),
            ],
            options={
                'ordering': ['-discipline'],
                'verbose_name': 'Video Progress',
                'verbose_name_plural': 'Video Progress',
            },
            bases=(models.Model,),
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
            name='TeacherKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=askmath.models.access.registerkey.generate_key, max_length=100, verbose_name='Key *')),
                ('in_use', models.BooleanField(default=False, verbose_name='In Use')),
                ('creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creator', models.ForeignKey(verbose_name='Person *', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='Teacher', blank=True, to='askmath.Teacher', null=True)),
            ],
            options={
                'ordering': ['user'],
                'verbose_name': 'Teacher Key',
                'verbose_name_plural': 'Teachers Key',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(help_text='Choose the position which is video belongs.', null=True, verbose_name='Position', blank=True)),
                ('title', models.CharField(help_text='Choose a title for video is.', max_length=50, verbose_name='Title')),
                ('description', models.TextField(help_text='Choose a description for video is.', null=True, verbose_name='Description', blank=True)),
                ('file', models.FileField(help_text='Perform upload a file.', upload_to=b'documents/video/%Y/%m/%d', verbose_name='File')),
                ('color', models.CharField(default=askMathPlus.components_metro.generate_color, max_length=50, verbose_name='Color')),
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
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='studentvideoprogress',
            name='video',
            field=models.ForeignKey(verbose_name='Video', to='askmath.Video'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='deficiencys',
            field=models.ManyToManyField(help_text='Choose possible deficiencies that the student may have if he opts for this item.', to='askmath.Lesson', null=True, verbose_name='Deficiencys', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpquestionshistoric',
            name='lesson',
            field=models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpquestionshistoric',
            name='question',
            field=models.ForeignKey(verbose_name='Question', to='askmath.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assistantkey',
            name='creator',
            field=models.ForeignKey(verbose_name='Person *', to=settings.AUTH_USER_MODEL),
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
            field=models.ForeignKey(verbose_name='Discipline', to='askmath.Discipline'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answeredquestionshistoric',
            name='items',
            field=models.ManyToManyField(to='askmath.Item', verbose_name='Items'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answeredquestionshistoric',
            name='lesson',
            field=models.ForeignKey(verbose_name='Lesson', to='askmath.Lesson'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answeredquestionshistoric',
            name='question',
            field=models.ForeignKey(verbose_name='Question', to='askmath.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='administratorkey',
            name='creator',
            field=models.ForeignKey(verbose_name='Person *', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='administratorkey',
            name='user',
            field=models.ForeignKey(related_name='Administrator', blank=True, to='askmath.Administrator', null=True),
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
