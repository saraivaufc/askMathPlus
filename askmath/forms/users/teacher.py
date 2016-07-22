# -*- coding: UTF-8 -*-
from askmath.models import Teacher
from .person import RegisterForm


class TeacherForm(RegisterForm):
    class Meta(RegisterForm.Meta):
        model = Teacher
