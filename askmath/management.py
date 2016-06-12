from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission
from django.db.models import signals
from askmath.models.users import Person, Administrator, Teacher, Assistant, Student 
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save

import models

permissions = {
    "access_manager": "Access Manager",
    "access_content": "Access Content",
    
    "access_manager_person": "Access Manager Person",
    "read_person": "Read Person",
    "write_person": "Write Person",
    "write_administrator": "Write Administrator",
    "write_teacher": "Write Teacher",
    "write_assistant": "Write Assistant",
    "write_student": "Write Student",
    
    
    "access_manager_student_historic": "Access Manager Student Historic",
    "read_student_historic": "Read StudentHistoric",
    "write_student_historic": "Write StudentHistoric",
    
    "access_manager_student_progress": "Access Manager Student Progress",
    "read_student_progress": "Read StudentProgress",
    "write_student_progress": "Write StudentProgress",
    
    "access_manager_student_state": "Access Manager Student State",
    "read_student_state": "Read StudentState",
    "write_student_state": "Write StudentState",
    
    "access_manager_statistics": "Access Manager Statistics",
    "read_statistics": "Read Statistics",
    "write_statistics": "Write Statistics",
    
    "access_manager_classe": "Access Manager Classe",
    "read_classe": "Read Classe",
    "write_classe": "Write Classe",

    "access_manager_discipline": "Access Manager Discipline",
    "read_discipline": "Read Discipline",
    "write_discipline": "Write Discipline",
    
    "access_manager_lesson": "Access Manager Lesson",
    "read_lesson": "Read Lesson",
    "write_lesson": "Write Lesson",
    
    "access_manager_question": "Access Manager Question",
    "read_question": "Read Question",
    "write_question": "Write Question",
    
    "access_manager_video": "Access Manager Video",
    "read_video": "Read Video",
    "write_video": "Write Video",
    
    "access_manager_message": "Access Manager Message",
    "read_message": "Read Message",
    "write_message": "Write Message",
    
    
    "access_forum_admin": "Access Forum Admin",
    "read_category": "Read Category",
    "write_category": "Write Category",
    
    "read_topic": "Read Topic",
    "write_topic": "Write Topic",
    
    "read_comment": "Read Comment",
    "write_comment": "Write Comment",  
}

group_permissions = {
    "administrator": [
        "access_manager",
        
        "access_manager_person",
        "read_person",
        "write_person",
        "write_administrator",
        "write_teacher",
        "write_assistant",
        
        "access_manager_student_historic",
        "read_student_historic",
        "write_student_historic",
        
        "access_manager_student_progress",
        "read_student_progress",
        "write_student_progress",
        
        "access_manager_student_state",
        "read_student_state",
        "write_student_state",
        
        "access_manager_statistics",
        "read_statistics",
        "write_statistics",
        
        "access_manager_classe",
        "read_classe",
        "write_classe",

        "access_manager_discipline",
        "read_discipline",
        "write_discipline",
        
        "access_manager_lesson",
        "read_lesson",
        "write_lesson",
        
        "access_manager_question",
        "read_question",
        "write_question",
        
        "access_manager_video",
        "read_video",
        "write_video",
        
        "access_manager_message",
        "read_message",
        "write_message",
        
        "access_forum_admin",
        "read_category",
        "write_category",
        "read_topic",
        "write_topic",
        "read_comment",
        "write_comment",
        
    ],
    "teacher": [
        "access_manager",
        
        "access_manager_person",
        "read_person",
        "write_person",
        "write_teacher",
        "write_assistant",
        
        "access_manager_student_historic",
        "read_student_historic",
        
        "access_manager_student_progress",
        "read_student_progress",
        
        "access_manager_student_state",
        "read_student_state",
        
        "access_manager_statistics",
        "read_statistics",

        "access_manager_classe",
        "read_classe",
        "write_classe",
        
        "access_manager_discipline",
        "read_discipline",
        "write_discipline",
        
        "access_manager_lesson",
        "read_lesson",
        "write_lesson",
        
        "access_manager_question",
        "read_question",
        "write_question",
        
        "access_manager_video",
        "read_video",
        "write_video",
        
        "access_manager_message",
        "read_message",
        "write_message",
        
        "access_forum_admin",
        "read_category",
        "write_category",
        "read_topic",
        "write_topic",
        "read_comment",
        "write_comment",
        
    ],
    "assistant": [
        "access_manager",

        "access_manager_discipline",
        "read_discipline",
        
        "access_manager_lesson",
        "read_lesson",
        
        "access_manager_question",
        "read_question",
        "write_question",
        
        "access_manager_video",
        "read_video",
        "write_video",
        
        "access_forum_admin",
        "read_category",
        "read_topic",
        "write_topic",
        "read_comment",
        "write_comment",
        
    ],
    "student": [
        "access_content",
        
        "read_person",
        
        "write_student_historic",
        
        "write_student_progress",
        
        "write_student_state",
        
        "read_classe",

        "read_discipline",
        
        "read_lesson",
        
        "read_question",
        
        "read_video",
        
        "read_category",
        "read_topic",
        "write_topic",
        "read_comment",
        "write_comment",
        
    ],
}

def create_user_groups(app, created_models, verbosity, **kwargs):
    if verbosity > 0:
        print "Initialising data post_syncdb"
    
    for group in group_permissions:
        if group == 'administrator':
            model = Administrator
        elif group == 'teacher':
            model = Teacher
        elif group == 'assistant':
            model = Assistant
        elif group == 'student':
            model = Student
        else:
            model = Student
        content_type = ContentType.objects.get_for_model(model)

        role, created = Group.objects.get_or_create(name=group)
        if verbosity > 1 and created:
            print 'Creating group', group
        for perm in group_permissions[group]:
            perm, created = Permission.objects.get_or_create(codename=perm, name=permissions[perm], content_type=content_type)
            role.permissions.add(perm)
            if verbosity > 1:
                print 'Permitting', group, 'to', perm
        role.save()

def default_group(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='student'))
post_save.connect(default_group, sender=User)



signals.post_syncdb.connect(
    create_user_groups, 
    sender=models,
    dispatch_uid='askmath.models.create_user_groups'
)