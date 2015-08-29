from django.db import models
from datetime import  datetime
from django.utils.translation import ugettext_lazy as _

class Comment(models.Model):
    person = models.ForeignKey('Person', verbose_name=_("Person"))
    topic = models.ForeignKey('Topic', verbose_name=_("Topic"))
    description = models.TextField(verbose_name=_("Description"))
    likes = models.ManyToManyField('Like', verbose_name=_("Likes"), null=True, blank=True)
    file = models.FileField(verbose_name=_("File"), upload_to = 'documents/forum/comment/%Y/%m/%d',
        help_text=_("Perform upload a file."), null=True, blank=True)
    
    creation = models.DateTimeField(verbose_name=_('Creation'), default=datetime.now)
    exists = models.BooleanField(verbose_name=_("Exists"), default=True)
    
    def get_person(self):
        return self.person
    
    def get_topic(self):
        return self.topic
    
    def get_description(self):
        return self.description
    
    def get_file(self):
        return self.file
    
    def get_likes(self):
        return self.likes.objects.filter(exists=True)
    
    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()
    
    def __unicode__(self):
        return self.description

    class Meta:
        ordering = ['creation']
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
