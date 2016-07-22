# -*- coding: UTF-8 -*-
from askmath.models import Administrator
from .person import RegisterForm


class AdministratorForm(RegisterForm):
    class Meta(RegisterForm.Meta):
        model = Administrator
