# -*- coding: UTF-8 -*-
from .person import RegisterForm
from askmath.models import Student


class StudentForm(RegisterForm):
    class Meta(RegisterForm.Meta):
        model= Student

 