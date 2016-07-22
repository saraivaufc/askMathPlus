from askMathPlus.settings import generate_color, COLORS_ALL
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _


class Topic(models.Model):
    person = models.ForeignKey('Person', verbose_name=_(u"Person"))
    category = models.ForeignKey('Category', verbose_name=_(u"Category"))
    title = models.CharField(verbose_name=_(u"Title"), max_length=255)
    description = models.TextField(verbose_name=_(u"Description"),
        help_text=_(u"Choose a description for the topic."))
    likes = models.ManyToManyField('Like', verbose_name=_(u"Likes"), null=True, blank=True)
    file = models.FileField(verbose_name=_(u"File"), upload_to = 'documents/forum/topic/%Y/%m/%d',
        help_text=_(u"Perform upload a file."), null=True, blank=True)
    
    color = models.CharField(verbose_name=_('Color'), max_length=50, default=generate_color, choices=COLORS_ALL,
        help_text=_(u"Choose a color for the topic."))
    creation = models.DateTimeField(verbose_name=_('Creation'), default=timezone.now)
    exists = models.BooleanField(verbose_name=_(u"Exists"), default=True)
    
    
    def get_person(self):
        return self.person
    
    def get_category(self):
        return self.category
    
    def get_title(self):
        return self.title

    def get_description(self):
        return self.description
    
    def get_likes(self):
        return self.likes.filter(exists=True)
    
    def get_likes_persons(self):
        persons = []
        for like in self.get_likes():
            persons.append(like.get_person())
        return persons
    
    def get_comments(self):
        from askmath.models.comment import Comment
        comments = Comment.objects.filter(exists=True, topic=self.id)
        return comments
    
    def get_comments_persons(self):
        persons = []
        for comment in self.get_comments():
            persons.append(comment.get_person())
        return persons
    
    def like(self, person):
        from askmath.models import Like
        try:
            like = Like.objects.create(person=person)
            self.likes.add(like)
            return True
        except:
            return False
        
    def unlike(self, person):
        try:
            self.likes.filter(person=person).delete()
            return True
        except:
            return False
    
    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()
    
    def __unicode__(self):
        return self.description

    class Meta:
        ordering = ['-creation']
        verbose_name = _(u"Topic")
        verbose_name_plural = _(u"Topics")
