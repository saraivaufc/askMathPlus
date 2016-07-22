# -*- coding: UTF-8 -*-
from askmath.models import Student
from .person import RegisterForm


class StudentForm(RegisterForm):
    class Meta(RegisterForm.Meta):
        model = Student
