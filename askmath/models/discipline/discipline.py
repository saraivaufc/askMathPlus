from datetime import datetime
from django.db import models
from django.utils.translation import ugettext as _

from askmath.models.lesson import Lesson

from .idiscipline import IDiscipline


class Discipline(IDiscipline):
    title = models.CharField(verbose_name=_("Title"), max_length=100,
        help_text=_("Choose a title for the discipline."))
    responsible = models.CharField(verbose_name=_("Responsible"), max_length=100,null=True, blank=True,
        help_text=_("Choose responsible for the discipline.") )
    
    visible = models.BooleanField(verbose_name=_("Visible"), default=False,
        help_text=_("Select this option to leave visible discipline at all."))
    creation = models.DateTimeField(verbose_name=_('Creation'), default=datetime.now)
    exists = models.BooleanField(verbose_name=_("Exists"), default=True)
    
    def get_title(self):
        return self.title
    
    def get_responsible(self):
        return self.responsible
    
    def get_lessons(self, visible=None): 
        lessons = Lesson.objects.filter(exists=True, disciplines = self.id)
        return lessons
    
    def get_lessons_visible(self):
        lessons = Lesson.objects.filter(exists=True,visible=True,disciplines = self.id)
        return lessons
    
    def get_lessons_removed(self):
        lessons = Lesson.objects.filter(exists=False,disciplines = self.id)
        return lessons

    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()
        
    def is_visible(self):
        return self.visible
    
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = _("Discipline")
        verbose_name_plural = _("Disciplines")