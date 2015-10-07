#-*- encoding=UTF-8 -*-


from datetime import datetime
from django.db import models
from django.utils.translation import ugettext as _
from askMathPlus.settings import generate_color, COLORS_ALL
from askmath.models.question import Question
from askmath.models.video import Video

class Lesson(models.Model):
    discipline = models.ForeignKey("Discipline",verbose_name=_(u"Discipline"), null=False, blank=False,
        help_text=_(u"Choose the discipline which is lesson belongs."))
    title = models.CharField(verbose_name=_(u"Title"), max_length=50,
        help_text=_(u"Choose a title for lesson is."))
    description = models.TextField(verbose_name=_(u"Description"),
        help_text=_(u"Choose a description for lesson is."))
    requirements = models.ManyToManyField("Lesson",verbose_name=_(u"Requirements") , related_name="Requirements", null=True, blank=True,
        help_text=_(u"Choose the lessons is recommended completion before continuing this."))
    sugestions = models.ManyToManyField("Lesson",verbose_name=_(u"Sugestions") , related_name="Sugestions", null=True, blank=True, 
        help_text=_(u"Choose the lessons is recommended pursue after completing this."))
    maximum_hops = models.IntegerField(verbose_name=_(u"Maximum Hops"),
        help_text=_(u"Choose the maximum number of hops that the student can perform this lesson."))
    
    color = models.CharField(verbose_name=_('Color'), max_length=50, default=generate_color, choices=COLORS_ALL,
        help_text=_(u"Choose a color for the lesson."))
    visible = models.BooleanField(default=False,
        help_text=_(u"Select this option to leave visible lesson at all."))
    creation = models.DateTimeField(_('Creation'), default=datetime.now)
    exists = models.BooleanField(default=True)

    def get_discipline(self):
        return self.discipline
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_requirements(self):
        return self.requirements.filter(exists=True)
    
    def get_sugestions(self):
        return self.sugestions.filter(exists=True) 
    
    def get_maximum_hops(self):
        return self.maximum_hops
    
    def get_questions(self):
        questions = Question.objects.filter(exists=True,lesson = self.id)
        if questions:
            questions = list(questions)
            questions.sort()
        return questions
    
    def get_questions_visibles(self):
        questions = Question.objects.filter(exists=True,visible=True , lesson = self.id)
        if questions:
            questions = list(questions)
            questions.sort()
        return questions
    
    def get_questions_removed(self):
        questions = Question.objects.filter(exists=False,lesson = self.id)
        if questions:
            questions = list(questions)
            questions.sort()
        return questions
    
    def get_videos(self):
        videos = Video.objects.filter(exists=True,lesson = self.id)
        if videos:
            videos = list(videos)
            videos.sort()
        return videos
    
    def get_videos_visibles(self):
        videos = Video.objects.filter(exists=True,visible=True, lesson = self.id)
        return videos
    
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
            verbose_name = _(u"Lesson")
            verbose_name_plural = _(u"Lessons")

    