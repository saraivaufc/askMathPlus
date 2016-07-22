# -*- coding: UTF-8 -*-
from askmath.models import Assistant
from .person import RegisterForm


class AssistantForm(RegisterForm):
    class Meta(RegisterForm.Meta):
        model = Assistant
