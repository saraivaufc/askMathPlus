# -*- coding: UTF-8 -*-
from .person import RegisterForm
from askmath.models import Administrator


class AdministratorForm(RegisterForm):
    
    class Meta(RegisterForm.Meta):
        model= Administrator