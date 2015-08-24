from datetime import datetime
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.crypto import get_random_string

def generate_key():
    return get_random_string(length=6)

class RegisterKey(models.Model):
    creator = models.ForeignKey("Person", verbose_name=_("Person *"))
    key = models.CharField(max_length=100, verbose_name=_("Key *"), default=generate_key)
    in_use = models.BooleanField(default=False, verbose_name=_("In Use"))
    
    creation = models.DateTimeField(verbose_name=_('Creation'), default=datetime.now)
    exists = models.BooleanField(verbose_name=_("Exists"), default=True)
        
    
    def get_creator(self):
        return self.creator
    
    def get_key(self):
        return self.key
    
    def __unicode__(self):
        return self.key
    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()
    
    class Meta:
        abstract = True
        ordering = ['creator']
        verbose_name = _("Register Key")
        verbose_name_plural = _("Register Keys")