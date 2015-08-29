from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime

class Like(models.Model):
    person = models.ForeignKey('Person', verbose_name=_("Person"))
    
    creation = models.DateTimeField(verbose_name=_('Creation'), default=datetime.now)
    exists = models.BooleanField(verbose_name=_("Exists"), default=True)
    
    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()
    
    def __unicode__(self):
        return self.person

    class Meta:
        ordering = ['creation']
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")

    