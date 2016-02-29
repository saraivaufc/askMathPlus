# -*- coding: UTF-8 -*-
from .person import RegisterForm
from askmath.models import Teacher


class TeacherForm(RegisterForm):
    
    class Meta(RegisterForm.Meta):
        model= Teacher