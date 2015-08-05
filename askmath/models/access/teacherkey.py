from askmath.models.access.registerkey import RegisterKey
from django.db import models
class TeacherKey(RegisterKey):
    user = models.ForeignKey("Teacher",related_name="Teacher", null=True, blank=True)