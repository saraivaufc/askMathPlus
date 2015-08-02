# -*- coding: UTF-8 -*-
from askmath.forms.users.person import PersonForm
from askmath.models import Teacher


class TeacherForm(PersonForm):
    
    class Meta(PersonForm.Meta):
        model= Teacher