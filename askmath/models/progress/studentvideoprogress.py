from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

class StudentVideoProgress(models.Model):
    student = models.ForeignKey('Student', verbose_name=_(u"Student"))
    discipline = models.ForeignKey('Discipline', verbose_name=_(u"Discipline"))
    lesson = models.ForeignKey('Lesson', verbose_name=_(u"Lesson"))
    video = models.ForeignKey('Video', verbose_name=_(u"Video"))
    
    exists= models.BooleanField(default=True, verbose_name=_(u"Exists"))
    creation = models.DateTimeField(verbose_name=_('Creation'), default=timezone.now)
    
    def get_discipline(self):
        return self.discipline
    
    def get_lesson(self):
        return self.lesson
    
    def get_video(self):
        return self.video

    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()

    
    class Meta:
        ordering = ['-discipline']
        verbose_name = _(u"Video Progress")
        verbose_name_plural = _(u"Video Progress")