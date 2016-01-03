# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
from django.utils import timezone
from askMathPlus import settings
from django.contrib.auth.models import Group, Permission

try:
    from hashlib import md5
except:
    from md5 import new as md5
        
class Person(User):
    profile_image = models.ImageField(verbose_name=_(u"Profile Image"),help_text=_(u"Please enter you profile image."),upload_to = 'documents/image/profile_image/%Y/%m/%d', null=True, blank=True, default=None)
    color = models.CharField(verbose_name=_(u'Color'), max_length=50, default=settings.generate_color)
    creation = models.DateTimeField(_(u'Creation'), default=timezone.now)
    exists = models.BooleanField(default = True)

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_name(self):
        return self.get_first_name() +" "+ self.get_last_name()

    def get_email(self):
        return self.email

    def save(self,group=None, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)
        if not group:
            group = 'student'
        print "Add person in",group
        group = Group.objects.get(name=group)
        self.groups.add(group)

    def get_profile_image(self):
        return self.profile_image
    
    def __unicode__(self):
        return self.get_name()
    
    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()
    
    class Meta(User.Meta):
        ordering = ['-date_joined', ]
        verbose_name = _(u'person')
        verbose_name_plural = _(u'persons')
