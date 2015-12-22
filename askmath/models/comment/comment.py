from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class Comment(models.Model):
    person = models.ForeignKey('Person', verbose_name=_(u"Person"))
    topic = models.ForeignKey('Topic', verbose_name=_(u"Topic"))
    description = models.TextField(verbose_name=_(u"Comment"))
    likes = models.ManyToManyField('Like', verbose_name=_(u"Likes"), null=True, blank=True)
    creation = models.DateTimeField(verbose_name=_(u'Creation'), default=timezone.now)
    exists = models.BooleanField(verbose_name=_(u"Exists"), default=True)
    
    def get_person(self):
        return self.person
    
    def get_topic(self):
        return self.topic
    
    def get_description(self):
        return self.description
    
    def get_file(self):
        return self.file
    
    def get_likes(self):
        return self.likes.filter(exists=True)
    
    def get_likes_persons(self):
        persons = []
        for like in self.get_likes():
            persons.append(like.get_person())
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
        ordering = ['creation']
        verbose_name = _(u"Comment")
        verbose_name_plural = _(u"Comments")
