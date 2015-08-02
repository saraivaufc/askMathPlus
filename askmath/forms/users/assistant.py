# -*- coding: UTF-8 -*-
from askmath.forms.users.person import PersonForm
from askmath.models import Assistant


class AssistantForm(PersonForm):
    class Meta(PersonForm.Meta):
        model= Assistant