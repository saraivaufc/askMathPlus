from django.db import models


class IVideo(models.Model):
    def delete(self):
        pass
        
    def restore(self):
        pass
    
    def convert(self):
        pass

    def get_extension(self):
        pass