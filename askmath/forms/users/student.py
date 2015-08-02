# -*- coding: UTF-8 -*-
from askmath.forms.users.person import PersonForm
from askmath.models import Student


class StudentForm(PersonForm):
    class Meta(PersonForm.Meta):
        model= Student