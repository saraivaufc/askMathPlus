from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime

class SkippedQuestionsHistoric(models.Model):
    discipline = models.ForeignKey('Discipline', verbose_name=_("Discipline"))
    lesson = models.ForeignKey('Lesson', verbose_name=_("Lesson"))
    question = models.ForeignKey('Question', verbose_name=_("Question"))
    
    exists= models.BooleanField(default=True, verbose_name=_("Exists"))
    creation = models.DateTimeField(verbose_name=_('Creation'), default=datetime.now)
    
    def get_discipline(self):
        return self.discipline
    
    def get_lesson(self):
        return self.lesson
    
    def get_question(self):
        return self.question
    
    def __unicode__(self):
        return unicode(self.discipline) + ' - ' + unicode(self.lesson) + ' - ' + unicode(self.question)
    
    
    class Meta:
        ordering = ['-discipline']
        verbose_name = _("Skipped Question Historic")
        verbose_name_plural = _("Skipped Questions Historic")