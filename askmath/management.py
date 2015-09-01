from django.contrib.auth.models import Group, Permission
from django.db.models import signals

import models


askmath_group_permissions = {
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
        
        "access_manager_contact",
        "read_contact",
        "write_contact",
        
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
        
        "access_manager_contact",
        "read_contact",
        "write_contact",
        
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
    
    for group in askmath_group_permissions:
        role, created = Group.objects.get_or_create(name=group)
        if verbosity > 1 and created:
            print 'Creating group', group
        for perm in askmath_group_permissions[group]:
            role.permissions.add(Permission.objects.get(codename=perm))
            if verbosity > 1:
                print 'Permitting', group, 'to', perm
        role.save()

signals.post_syncdb.connect(
    create_user_groups, 
    sender=models,
    dispatch_uid='askmath.models.create_user_groups'
)