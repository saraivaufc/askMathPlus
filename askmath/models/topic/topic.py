from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime
from askMathPlus.settings import generate_color

class Topic(models.Model):
    person = models.ForeignKey('Person', verbose_name=_("Person"))
    category = models.ForeignKey('Category', verbose_name=_("Category"))
    title = models.CharField(verbose_name=_("Title"), max_length=255,
        help_text=_("Choose a title for the topic."))
    description = models.TextField(verbose_name=_("Description"),
        help_text=_("Choose a description for the topic."))
    likes = models.ManyToManyField('Like', verbose_name=_("Likes"), null=True, blank=True)
    file = models.FileField(verbose_name=_("File"), upload_to = 'documents/forum/topic/%Y/%m/%d',
        help_text=_("Perform upload a file."), null=True, blank=True)
    
    color = models.CharField(verbose_name=_('Color'), max_length=50, default=generate_color)
    creation = models.DateTimeField(verbose_name=_('Creation'), default=datetime.now)
    exists = models.BooleanField(verbose_name=_("Exists"), default=True)
    
    
    def get_person(self):
        return self.person
    
    def get_category(self):
        return self.category
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_likes(self):
        return self.likes.objects.filter(exists=True)
    def get_comments(self):
        from askmath.models.comment import Comment
        comments = Comment.objects.filter(exists=True, topic=self.id)
        return comments
    
    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()
    
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-creation']
        verbose_name = _("Topic")
        verbose_name_plural = _("Topics")
