# -*- coding: UTF-8 -*-
from askmath.forms.users.person import PersonForm
from askmath.models import Administrator


class AdministratorForm(PersonForm):
    
    class Meta(PersonForm.Meta):
        model= Administrator