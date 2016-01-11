from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

class Like(models.Model):
    person = models.ForeignKey('Person', verbose_name=_(u"Person"))
    
    creation = models.DateTimeField(verbose_name=_('Creation'), default=timezone.now)
    exists = models.BooleanField(verbose_name=_(u"Exists"), default=True)
    
    def get_person(self):
        return self.person
    
    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()
    
    def __unicode__(self):
        return unicode(self.person)

    class Meta:
        ordering = ['creation']
        verbose_name = _(u"Like")
        verbose_name_plural = _(u"Likes")

    