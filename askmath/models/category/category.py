from django.db import models
from datetime import datetime
from django.utils.translation import ugettext as _
from askMathPlus.settings import generate_color, COLORS_ALL

class Category(models.Model):
    person = models.ForeignKey('Person', verbose_name=_("Person"))
    title = models.CharField(verbose_name=_("Title"), max_length=100,
        help_text=_("Choose a title for the category."))
    description = models.TextField(verbose_name=_("Description"), max_length=100,null=True, blank=True,
        help_text=_("Choose a description for the category."))
    color = models.CharField(verbose_name=_('Color'), max_length=50, default=generate_color, choices=COLORS_ALL,
        help_text=_("Choose a color for the category."))
    creation = models.DateTimeField(verbose_name=_('Creation'), default=datetime.now)
    exists = models.BooleanField(verbose_name=_("Exists"), default=True)
    
    def get_person(self):
        return self.person
    
    def get_topics(self):
        from askmath.models.topic import Topic
        topics = Topic.objects.filter(exists=True, category=self.id)
        return topics
    
    def get_topics_removed(self):
        from askmath.models.topic import Topic
        topics = Topic.objects.filter(exists=False, category=self.id)
        return topics
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description

    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()
    
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
