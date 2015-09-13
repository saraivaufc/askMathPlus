#-*- encoding=UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime
from askMathPlus.settings import generate_color

class Contact(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=100,
        help_text=_("Enter yout name."))
    email = models.EmailField(verbose_name=_("Email"), max_length=254,
        help_text=_("Enter yout email."))
    message = models.TextField(verbose_name=_("Message"), max_length=2000, 
        help_text=_("Your use here tags HTML: <a href="" title=""> <abbr title=""> <acronym title=""> <b> <blockquote cite=""> <cite> <code> <del datetime=""> <em> <i> <q cite=""> <strike> <strong> "))
    file = models.FileField(verbose_name=_("File"), upload_to = 'documents/contact_files/%Y/%m/%d',
        help_text=_("Perform upload a file."), null=True, blank=True)

    color = models.CharField(verbose_name=_('Color'), max_length=50, default=generate_color)
    creation = models.DateTimeField(verbose_name=_('Creation'), default=datetime.now)
    exists = models.BooleanField(verbose_name=_("Exists"), default=True)
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_message(self):
        return self.message
    
    def get_file(self):
        return self.file
    
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
