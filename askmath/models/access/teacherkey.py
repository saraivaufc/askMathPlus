from askmath.models.access.registerkey import RegisterKey
from django.utils.translation import ugettext as _
from django.db import models

class TeacherKey(RegisterKey):
    user = models.ForeignKey("Teacher",related_name="Teacher", null=True, blank=True)
    
    def get_user(self):
        return self.user
    
    def add_user(self, user):
        self.user = user
        self.in_use = True
        self.save()
        
    class Meta:
        ordering = ['user']
        verbose_name = _(u"Teacher Key")
        verbose_name_plural = _(u"Teachers Key")