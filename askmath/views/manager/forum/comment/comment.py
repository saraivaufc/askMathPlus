from .icomment import IComment
from askmath.models import Comment as CommentModel
from django.template import Context, Template
from django.http.response import HttpResponse
class Comment(IComment):
    def add_comment(self, request, category, topic, comment, message=None):
        pass
    def remove_comment(self):
        pass
    
    def edit_comment(self):
        pass