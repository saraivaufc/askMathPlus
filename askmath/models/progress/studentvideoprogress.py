from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime

class StudentVideoProgress(models.Model):
    student = models.ForeignKey('Student', verbose_name=_("Student"))
    discipline = models.ForeignKey('Discipline', verbose_name=_("Discipline"))
    lesson = models.ForeignKey('Lesson', verbose_name=_("Lesson"))
    video = models.ForeignKey('Video', verbose_name=_("Video"))
    
    exists= models.BooleanField(default=True, verbose_name=_("Exists"))
    creation = models.DateTimeField(verbose_name=_('Creation'), default=datetime.now)
    
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
        verbose_name = _("Video Progress")
        verbose_name_plural = _("Video Progress")