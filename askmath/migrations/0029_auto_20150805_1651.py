# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askmath', '0028_auto_20150805_1627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permissions',
            options={'permissions': (('access_manager', 'Access Manager'), ('access_manager_person', 'Access Manager Person'), ('read_person', 'Read Person'), ('write_person', 'Write Person'), ('write_administrator', 'Write Administrator'), ('write_teacher', 'Write Teacher'), ('write_assistant', 'Write Assistant'), ('write_student', 'Write Student'), ('access_manager_student_historic', 'Access Manager Student Historic'), ('read_student_historic', 'Read StudentHistoric'), ('write_student_historic', 'Write StudentHistoric'), ('access_manager_student_progress', 'Access Manager Student Progress'), ('read_student_progress', 'Read StudentProgress'), ('write_student_progress', 'Write StudentProgress'), ('access_manager_student_state', 'Access Manager Student State'), ('read_student_state', 'Read StudentState'), ('write_student_state', 'Write StudentState'), ('access_manager_statistics', 'Access Manager Statistics'), ('read_statistics', 'Read Statistics'), ('write_statistics', 'Write Statistics'), ('access_manager_discipline', 'Access Manager Discipline'), ('read_discipline', 'Read Discipline'), ('write_discipline', 'Write Discipline'), ('access_manager_lesson', 'Access Manager Lesson'), ('read_lesson', 'Read Lesson'), ('write_lesson', 'Write Lesson'), ('access_manager_question', 'Access Manager Question'), ('read_question', 'Read Question'), ('write_question', 'Write Question'), ('access_manager_video', 'Access Manager Video'), ('read_video', 'Read Video'), ('write_video', 'Write Video'))},
        ),
    ]
