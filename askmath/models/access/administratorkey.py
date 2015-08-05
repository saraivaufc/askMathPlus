from django.db import models
from django.utils.translation import ugettext as _
from askmath.models.access.registerkey import RegisterKey

class AdministratorKey(RegisterKey):
    user = models.ForeignKey("Administrator", related_name="Administrator", null=True, blank=True)
    
    def get_user(self):
        return self.user
    
    def add_user(self, user):
        self.user = user
        self.in_use = True
        self.save()
        
    class Meta:
        ordering = ['user']
        verbose_name = _("Administrator Key")
        verbose_name_plural = _("Administrators Key")