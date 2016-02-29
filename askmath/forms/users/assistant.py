# -*- coding: UTF-8 -*-
from .person import RegisterForm
from askmath.models import Assistant


class AssistantForm(RegisterForm):
    class Meta(RegisterForm.Meta):
        model= Assistant