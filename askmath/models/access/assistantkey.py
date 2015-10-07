from askmath.models.access.registerkey import RegisterKey
from django.utils.translation import ugettext as _
from django.db import models

class AssistantKey(RegisterKey):
    user = models.ForeignKey("Assistant",related_name="Assistant", null=True, blank=True)
    
    def get_user(self):
        return self.user
    
    def add_user(self, user):
        self.user = user
        self.in_use = True
        self.save()
        
    class Meta:
        ordering = ['user']
        verbose_name = _(u"Assistant Key")
        verbose_name_plural = _(u"Assistants Key")