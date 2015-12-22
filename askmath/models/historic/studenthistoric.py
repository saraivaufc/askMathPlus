from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

class StudentHistoric(models.Model):
    student = models.ForeignKey('Student', verbose_name=_(u"Student"))
    answered_questions_historic = models.ManyToManyField('AnsweredQuestionsHistoric', verbose_name=_(u"Answered Questions Historic"),related_name=_(u"Answered Questions Historic"), null=True, blank=True)
    help_questions_historic = models.ManyToManyField('HelpQuestionsHistoric',related_name=("Help Question Historic"),  verbose_name=_(u"Answered Questions Historic"), null=True, blank=True)
    skipped_questions_historic = models.ManyToManyField('SkippedQuestionsHistoric',related_name=("Skipped Question Historic"),  verbose_name=_(u"Answered Questions Historic"), null=True, blank=True)
    
    exists= models.BooleanField(default=True, verbose_name=_(u"Exists"))
    creation = models.DateTimeField(verbose_name=_('Creation'), default=timezone.now)
    
    def get_student(self):
        return self.student
    def get_answered_questions_historic(self):
        return self.answered_questions_historic.all()
    
    def get_help_questions_historic(self):
        return self.help_questions_historic.all()
    
    def get_skipped_questions_historic(self):
        return self.skipped_questions_historic.all()
    
    def __unicode__(self):
        return unicode(self.student)
    
    class Meta:
        ordering = ['-student']
        verbose_name = _(u"Student Historic")
        verbose_name_plural = _(u"Students Historic")