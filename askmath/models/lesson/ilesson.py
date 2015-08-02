from django.db import models


class ILesson(models.Model):
    def get_questions(self):
        pass
    
    def questions_visibles(self):
        pass
    
    def get_questions_removed(self):
        pass

    def get_videos(self):
        pass
    
    def get_disciplines(self):
        pass
    
    def get_requirements(self):
        pass
    
    def get_sugestions(self):
        pass
    
    def get_progress(self):
        pass

    
    def delete(self):
        pass
        
    def restore(self):
        pass
    