from django.utils.translation import ugettext as _

class ExperienceLevel():
    BEGINNER = _("Beginner")
    INTERMEDIATE = _("Intermediate")
    ADVANCED = _("Advanced")
    EXPERT = _("Expert")
    ASIAN = _("Asian")
    GOD = _("God")
    
    __LEVEL = None
        
    def __init__(self, LEVEL=1):
        if LEVEL == 1:
            self.__LEVEL = self.BEGINNER
        elif LEVEL == 2:
            self.__LEVEL = self.INTERMEDIATE
        elif LEVEL == 3:
            self.__LEVEL = self.ADVANCED
        elif LEVEL == 4:
            self.__LEVEL = self.EXPERT
        elif LEVEL == 5:
            self.__LEVEL = self.ASIAN
        elif LEVEL == 6:
            self.__LEVEL = self.GOD
        else:
            self.__LEVEL = self.BEGINNER
    def get_level(self):
        return self.__LEVEL

    def get_levels_all(self):
        levels = []
        levels.append(self.BEGINNER)
        levels.append(self.INTERMEDIATE)
        levels.append(self.ADVANCED)
        levels.append(self.EXPERT)
        levels.append(self.ASIAN)
        levels.append(self.GOD)
        return levels  
    
    def get_image_url(self):
        if self.__LEVEL == self.BEGINNER:
            return '/static/askmath/img/experience/BEGINNER.png'
        elif self.__LEVEL == self.INTERMEDIATE:
            return '/static/askmath/img/experience/INTERMEDIATE.png'
        elif self.__LEVEL == self.ADVANCED:
            return '/static/askmath/img/experience/ADVANCED.png'
        elif self.__LEVEL == self.EXPERT:
            return '/static/askmath/img/experience/EXPERT.png'
        elif self.__LEVEL == self.ASIAN:
            return '/static/askmath/img/experience/ASIAN.png'
        elif self.__LEVEL == self.GOD:
            return '/static/askmath/img/experience/GOD.png'
        else:
            return None
    
    def get_class_css(self):
        if self.__LEVEL == self.BEGINNER:
            return 'tag success'
        elif self.__LEVEL == self.INTERMEDIATE:
            return 'tag success'
        elif self.__LEVEL == self.ADVANCED:
            return 'tag info'
        elif self.__LEVEL == self.EXPERT:
            return 'tag info'
        elif self.__LEVEL == self.ASIAN:
            return 'tag warning'
        elif self.__LEVEL == self.GOD:
            return 'tag alert'
        else:
            return None