from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _


class AnsweredQuestionsHistoric(models.Model):
    discipline = models.ForeignKey('Discipline',related_name=_('Discipline'), verbose_name=_(u"Discipline"))
    lesson = models.ForeignKey('Lesson', related_name=_('Lesson'), verbose_name=_(u"Lesson"))
    question = models.ForeignKey('Question',related_name=_('Question'), verbose_name=_(u"Question"))
    item = models.ForeignKey('Item', related_name=_('Item'), verbose_name=_(u"Item"))
    hit = models.BooleanField(default=False, verbose_name=_(u"Hit"))
    
    exists= models.BooleanField(default=True, verbose_name=_(u"Exists"))
    creation = models.DateTimeField(verbose_name=_(u"Creation"), default=timezone.now)
    
    def get_discipline(self):
        return self.discipline
    
    def get_lesson(self):
        return self.lesson
    
    def get_question(self):
        return self.question
    
    def get_item(self):
        return self.item
    
    def get_hit(self):
        return self.hit
    
    def __unicode__(self):
        return unicode(self.discipline) + ' - ' + unicode(self.lesson) + ' - ' + unicode(self.question)
    
    
    class Meta:
        ordering = ['-discipline']
        verbose_name = _(u"Answered Question Historic")
        verbose_name_plural = _(u"Answered Questions Historic")