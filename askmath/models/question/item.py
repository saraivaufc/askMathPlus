#-*- encoding=UTF-8 -*-

from datetime import datetime
from django.db import models
from django.utils.translation import ugettext as _

class Item(models.Model):
    position = models.IntegerField(verbose_name=_("Position"), null=True,blank=True,
         help_text=_("Choose the position which is item belongs."))
    description = models.TextField(verbose_name=_("Description"), 
          help_text=_("Choose a description for item is."))
    correct = models.BooleanField(verbose_name=_("Is Correct"), default=False, 
        help_text=_("Say if this item is correct."))
    deficiencys = models.ManyToManyField('Lesson', verbose_name=_("Deficiencys"), null=True, blank=True,
        help_text=_("Choose possible deficiencies that the student may have if he opts for this item.")) 
    
    creation = models.DateTimeField(verbose_name=_('Creation'), default=datetime.now)
    exists = models.BooleanField(verbose_name=_("Exists"), default=True)
    
    
    def get_position(self):
        return self.position
    
    def get_description(self):
        return self.description
    
    def is_correct(self):
        return self.correct
    
    def get_deficiencys(self):
        return self.deficiencys.filter(exists=True)

    def __unicode__(self):
        return self.description[:30]
    
    def __ge__(self, other):
        return self.position >= other.position
    
    def __gt__(self, other):
        return self.position > other.position
    
    def __le__(self, other):
        return self.position <= other.position 
    
    def __lt__(self, other):
        return self.position < other.position

    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()

    class Meta:
        ordering = ['position']
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
