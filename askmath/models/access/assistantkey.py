from askmath.models.access.registerkey import RegisterKey
from django.db import models

class AssistantKey(RegisterKey):
    user = models.ForeignKey("Assistant",related_name="Assistant", null=True, blank=True)