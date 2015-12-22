# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
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

class AbstractSystemPerson(models.Model):
    location = models.CharField(_(u"location"), max_length=75, blank=True, null=True)
    last_seen = models.DateTimeField(_(u"last seen"), auto_now=True)
    last_ip = models.GenericIPAddressField(_(u"last ip"), blank=True, null=True)
    is_administrator = models.BooleanField(_('administrator status'), default=False,blank=True )
    is_moderator = models.BooleanField(_('moderator status'), default=False, blank=True)
    
    def get_location(self):
        return self.location
    
    def get_last_seen(self):
        return self.last_seen
    
    def get_last_ip(self):
        return self.last_ip
    
    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.is_administrator = True

        if self.is_administrator:
            self.is_teacher = True

        super(AbstractSystemPerson, self).save(*args, **kwargs)
        
    
    class Meta:
        abstract = True

class AbstractPerson(AbstractBaseUser, PermissionsMixin, AbstractSystemPerson):
    username = models.CharField(_(u"Username"), max_length=30, unique=True, db_index=True, help_text=_(u'Please enter you username.'),)
    name = models.CharField(_(u"Full Name "), max_length=100, blank=False,null=True,help_text=_(u'Please enter you full name.'),)
    email = models.EmailField(_(u"Email"), max_length=254, unique=True, blank=False, help_text=_(u'Please enter you email.'),)
    is_staff = models.BooleanField(_(u'staff status'), default=False,
                                   help_text=_(u'Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_(u'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_(u'date joined'), default=timezone.now)
    objects = UserManager()
    
    def get_short_name(self):
        if self.name:
            list_names = self.name.split(" ")
            if len(list_names) > 2:
                return list_names[0]+" "+list_names[len(list_names)-1]
            else:
                return " ".join(list_names)
        else:
            return self.username
    
    def get_username(self):
        return self.username
    
    def get_name(self):
        if self.name:
            return self.name
        else:
            return self.username
    
    def get_email(self):
        return self.email
    
    def get_date_joined(self):
        return self.date_joined
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]
    
    def __unicode__(self):
        return self.get_full_name()

    class Meta:
        abstract = True            
        
    def change_password(self, new_password):
        new_password_hash = md5(new_password).hexdigest()
        self.password = new_password_hash
        self.save()  
        
class Person(AbstractPerson):
    profile_image = models.ImageField(verbose_name=_(u"Profile Image"),help_text=_(u"Please enter you profile image."),upload_to = 'documents/image/profile_image/%Y/%m/%d', null=True, blank=True, default=None)
    color = models.CharField(verbose_name=_(u'Color'), max_length=50, default=settings.generate_color)
    creation = models.DateTimeField(_(u'Creation'), default=timezone.now)
    exists = models.BooleanField(default = True)

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)
        group = Group.objects.get(name=settings.DEFAULT_GROUP_NAME)
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
    
    class Meta(AbstractPerson.Meta):
        abstract = False
        db_table = 'auth_user'
        swappable = 'AUTH_USER_MODEL'
        app_label = 'askmath'
        ordering = ['-date_joined', ]
        verbose_name = _(u'person')
        verbose_name_plural = _(u'persons')
