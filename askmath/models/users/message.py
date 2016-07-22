# -*- encoding=UTF-8 -*-

from datetime import datetime

from askMathPlus.settings import generate_color
from django.db import models
from django.utils.translation import ugettext as _


class Message(models.Model):
    name = models.CharField(verbose_name=_(u"Name"), max_length=100,
                            help_text=_(u"Enter yout name."))
    email = models.EmailField(verbose_name=_(u"Email"), max_length=254,
                              help_text=_(u"Enter yout email."))
    message = models.TextField(verbose_name=_(u"Message"), max_length=2000,
                               help_text=_(
                                   u"Your use here tags HTML: <a href='' title=''> <abbr title=''> <acronym title=''> <b> <blockquote cite=''> <cite> <code> <del datetime=''> <em> <i> <q cite=''> <strike> <strong> "))
    file = models.FileField(verbose_name=_(u"File"), upload_to='documents/contact_files/%Y/%m/%d',
                            help_text=_(u"Perform upload a file."), null=True, blank=True)

    color = models.CharField(verbose_name=_(u"Color"), max_length=50, default=generate_color)
    creation = models.DateTimeField(verbose_name=_(u"Creation"), default=datetime.now)
    exists = models.BooleanField(verbose_name=_(u"Exists"), default=True)

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
        verbose_name = _(u"Message")
        verbose_name_plural = _(u"Messages")
