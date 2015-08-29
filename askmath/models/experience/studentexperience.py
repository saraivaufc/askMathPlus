from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime

class StudentExperience(models.Model):
    student = models.ForeignKey('Student', verbose_name=_("Student"))
    scores = models.IntegerField(default=0,verbose_name=_("Scores"))
    max_scores = models.IntegerField(default=10,verbose_name=_("Max Scores"))
    level = models.IntegerField(default=1,verbose_name=_("Level"))
    stars = models.IntegerField(default=0,verbose_name=_("Stars"))
    creation = models.DateTimeField(_('Creation'), default=datetime.now)
    exists = models.BooleanField(default=True)
    
    def get_student(self):
        return self.student
    def get_scores(self):
        return self.scores
    def get_level(self):
        return self.level
    def get_starts(self):
        return self.stars

       
    def up_scores(self, scores):
        self.scores = self.scores + scores
        if self.scores >= self.max_scores:
            self.scores = 0
            self.max_scores += self.max_scores
            self.up_stars()
        self.save()
    
    def down_scores(self, scores):
        self.scores = self.scores - scores
        if self.scores < 0:
            self.scores = 0
            self.down_stars()
        self.save()
    
    def up_stars(self):
        self.stars = self.stars + 1
        if self.stars >= 10:
            self.stars = 0
            self.max_scores += self.max_scores * 2
            self.up_level()
        self.save()
    
    def down_stars(self):
        self.stars = self.stars - 1
        if self.stars < 0:
            self.stars = 0
            self.down_level()
        self.save()
    
    def up_level(self):
        self.level = self.level + 1
        if self.level > 6:
            self.level=6;
        self.save()
    
    def down_level(self):
        self.level = self.level - 1
        self.stars = 0
        if self.level == 0:
            self.level = 1
        self.save()
            
    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()
    
    def __unicode__(self):
        return unicode(self.student)

    class Meta:
        ordering = ['-student']
        verbose_name = _("Student Experience")
        verbose_name_plural = _("Student Experiences")