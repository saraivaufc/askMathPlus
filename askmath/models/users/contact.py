#-*- encoding=UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime

class Contact(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=100)
    email = models.EmailField(verbose_name=_("Email"), max_length=254)
    subject = models.CharField(verbose_name=_("Subject"), max_length=100)
    message = models.TextField(verbose_name=_("Message"), max_length=2000)
    file = models.FileField(verbose_name=_("File"), upload_to = 'documents/contact_files/%Y/%m/%d',
        help_text=_("Perform upload a file."), null=True, blank=True)

    creation = models.DateTimeField(verbose_name=_('Creation'), default=datetime.now)
    exists = models.BooleanField(verbose_name=_("Exists"), default=True)
    
    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ['creation']
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
