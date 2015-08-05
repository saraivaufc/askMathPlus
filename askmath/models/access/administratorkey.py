from django.db import models
from askmath.models.access.registerkey import RegisterKey

class AdministratorKey(RegisterKey):
    user = models.ForeignKey("Administrator", related_name="Administrator", null=True, blank=True)