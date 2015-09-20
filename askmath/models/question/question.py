#-*- encoding=UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from askMathPlus.settings import generate_color, COLORS_ALL
from datetime import datetime

class Question(models.Model):
    lesson = models.ForeignKey('Lesson', verbose_name=_("Lesson"),
        help_text=_("Choose the lesson which is question belongs."))
    position = models.IntegerField(verbose_name=_("Position"),null=False,blank=False,
        help_text=_("Choose the position which is question belongs."))
    description = models.TextField(verbose_name=_("Description"), 
         help_text=_("Choose a description for question is."))
    items = models.ManyToManyField('Item', verbose_name=_("Items"),
         help_text=_("Choose items that this issue has."))
    help = models.TextField(verbose_name=_("Help"), null=True, blank=True, 
        help_text=_("Choose a help to this question."))
    
    SCORES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'),)
    scores=models.IntegerField(verbose_name=_("Scores"), choices=SCORES)
    
    color = models.CharField(verbose_name=_('Color'), max_length=50, default=generate_color, choices=COLORS_ALL,
        help_text=_("Choose a color for the question."))
    visible = models.BooleanField(verbose_name=_("Visible"), default=False,
        help_text=_("Select this option to leave visible question at all."))
    creation = models.DateTimeField(verbose_name=_('Creation'), default=datetime.now)
    exists = models.BooleanField(verbose_name=_("Exists"), default=True)
    
    def get_lesson(self):
        return self.lesson
    
    def get_position(self):
        questions_all = list(self.lesson.get_questions_visibles())
        if questions_all:
            questions_all.sort()
            for index, i in enumerate(questions_all):
                if i.id == self.id:
                    return index+1
        else:
            return -1
    
    def get_description(self):
        return self.description
    
    def get_items(self):
        return self.items.filter(exists=True)
    
    def get_items_corrects(self):
        return self.items.filter(exists=True, correct=True)
    
    def get_help(self):
        return self.help
    
    def get_scores(self):
        return self.scores
    
    def is_visible(self):
        return self.visible
    
    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()
    
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
        
    class Meta:
        ordering = ['position']
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")