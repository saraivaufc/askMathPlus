#-*- encoding=UTF-8 -*-


from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
from askmath.entities import TextMessage
from django.contrib import messages
from askmath.models.historic import StudentHistoric, AnsweredQuestionsHistoric, HelpQuestionsHistoric, SkippedQuestionsHistoric

class StudentLessonState(models.Model):
    student = models.ForeignKey('Student', verbose_name=_(u"Student"))
    discipline = models.ForeignKey('Discipline', verbose_name=_(u"Discipline"))
    lesson = models.ForeignKey('Lesson', verbose_name=_(u"Lesson"))
    scores = models.IntegerField(default=0,verbose_name=_(u"Scores"))
    remaining_jump = models.IntegerField(default=0,verbose_name=_(u"Remaining Jump"))
    hits_followed = models.IntegerField(default=0, verbose_name=_(u"Hits Followed"))
    errors_followed = models.IntegerField(default=0, verbose_name=_(u"Errors Followed"))
    percentage_completed= models.IntegerField(default=0, verbose_name=_(u"Percentage Completed"))
    
    answered_correct_questions = models.ManyToManyField('Question',related_name="Answered Correct Questions", verbose_name=_(u"Answered Questions"), null=True, blank=True)
    answered_incorrect_questions = models.ManyToManyField('Question',related_name="Answered Incorrect Questions", verbose_name=_(u"Answered Questions"), null=True, blank=True)
    skipped_questions = models.ManyToManyField('Question',related_name="Skipped Questions", verbose_name=_(u"Skipped Questions"), null=True, blank=True)
    help_questions = models.ManyToManyField('Question',related_name="Help Questions",verbose_name=_(u"Help Questions"), null=True, blank=True)
    
    exists= models.BooleanField(default=True, verbose_name=_(u"Exists"))
    creation = models.DateTimeField(verbose_name=_('Creation'), default=timezone.now)
    
    #GETS
    def get_student(self):
        return self.student
    
    def get_discipline(self):
        return self.discipline
    
    def get_lesson(self):
        return self.lesson
    
    def get_scores(self):
        return self.scores
    
    def get_remaining_jump(self):
        return self.remaining_jump
    
    def get_hits_followed(self):
        return self.hits_followed
    
    def get_errors_followed(self):
        return self.errors_followed
    
    def get_percentage_completed(self):
        return self.percentage_completed
    
    def get_answered_correct_questions(self):
        return self.answered_correct_questions.filter(exists = True, visible=True)
    
    def get_answered_incorrect_questions(self):
        return self.answered_incorrect_questions.filter(exists = True, visible=True)
    
    
    def get_skipped_questions(self):
        return self.skipped_questions.filter(exists=True, visible=True)
    
    def get_help_questions(self):
        return self.help_questions.filter(exists=True, visible=True)
    
    def get_question(self,last_question=None, definitive=False):
        print "\nLasta question:", last_question
        questions_all = list(self.lesson.get_questions_visibles())
        print "QUestions ALL:", questions_all
        answered_correct_questions = list(self.get_answered_correct_questions()) 
        print "Questoes corretas:", answered_correct_questions
        answered_incorrect_questions = list(self.get_answered_incorrect_questions())
        print "QUestoes incorretas:", answered_incorrect_questions
        skipped_questions = list(self.get_skipped_questions())
        print "Questoes Saltos:", skipped_questions
        
        questions_all = set(questions_all)
        answered_correct_questions = set(answered_correct_questions)
        answered_incorrect_questions = set(answered_incorrect_questions)
        skipped_questions = set(skipped_questions)
        last_question_list = set([last_question,])
        
        questions_remaining = (((questions_all.difference(answered_correct_questions)).difference(answered_incorrect_questions)).difference(skipped_questions)).difference(last_question_list);
        
        if last_question in skipped_questions: skipped_questions.remove(last_question)
        if last_question in answered_incorrect_questions: answered_incorrect_questions.remove(last_question) 
        
        questions = None
        if questions_remaining:
            print "Se tiver questoes restantes para serem respondidas..."
            questions = list(questions_remaining)
        elif skipped_questions and not answered_incorrect_questions:
            print "Se existir mais de duas questoes saltadas e nenhuma que foi respondida incorretamente..."
            questions = list(skipped_questions)
        elif answered_incorrect_questions and not skipped_questions:
            print "Se existir mais de duas questoes que foram respondidas incorretamente e nao existir nenhuma que foi saltada"
            questions = list(answered_incorrect_questions)
        elif skipped_questions and answered_incorrect_questions:
            print "cobra"
            questions = list(skipped_questions)
        elif not skipped_questions and not answered_incorrect_questions and last_question in answered_correct_questions:
            print "Se não existir mais nenhuma questao saltada e nem que foi respondida errada e a questao en questao ja tiver sido resolvida"    
            return None
        elif not skipped_questions and not answered_incorrect_questions and not last_question in answered_correct_questions:
            print "javali"    
            questions = [last_question,]
            
        if questions:      
            questions.sort()
            question = questions[0]
            if question in self.get_skipped_questions() and definitive:
                self.remove_skipped_question(question)
                print "Cavalo7"
            print "Cavalo9"
            return question
        else:
            print "Cavalo9"
            return None
    
    
    def update_percentage_completed(self):
        try:
            self.percentage_completed = (len(self.get_answered_correct_questions()) * 100)/ len(self.lesson.get_questions_visibles())
        except ZeroDivisionError:
            self.percentage_completed = 100
        if self.percentage_completed == 0:
            if not self.get_question():
                self.percentage_completed = 100;
        self.save()
        
    def up_scores(self, scores):
        if type(scores) == int:
            self.scores += scores
            self.save()
            return True
        else:
            return False
        
    def down_scores(self, scores):
        if type(scores) == int:
            self.scores -= scores
            if self.scores < 0:
                self.scores = 0
            self.save()
            return True
        else:
            return False
    
    def up_remaining_jump(self):
        self.remaining_jump += 1
        self.save()
        
    def down_remaining_jump(self):
        self.remaining_jump -= 1
        if self.remaining_jump < 0:
            self.remaining_jump = 0
        self.save()
    
    def add_answered_correct_question(self, question):
        #Se a licao ja tiver sido concluida
        if not self.get_question(question):
            return
        
        #Se a questao ja tinha sido respondida corretamente antes
        if question in self.get_answered_correct_questions():
            return
        
        #Se a questao ja tinha sido respondida incorretamente antes
        if question in self.get_answered_incorrect_questions():
            self.remove_answered_incorrect_questions(question)
            scores = question.scores/2
        else:
            scores = question.scores
        
        #Se a questao ja tinha sido saltada antes
        if question in self.get_skipped_questions():
            self.remove_skipped_question(question)
    
        self.answered_correct_questions.add(question)
        self.up_scores(scores)
        self.up_student_experience(scores)
        self.update_percentage_completed()
        self.save()
    
    def add_answered_incorrect_question(self, question):
        #Se a licao ja tiver sido concluida
        if not self.get_question(question):
            return
        
        #Se a quesao ja tinha sido respondida corretamente antes
        if question in self.get_answered_correct_questions():
            return
        
        #Se a questao ja tinha sido respondida incorretamente antes
        if question in self.get_answered_incorrect_questions():
            return
        
        #Se a questao ja tinha sido saltada antes
        if question in self.get_skipped_questions():
            self.remove_skipped_question(question)
        scores = question.scores/2
        self.answered_incorrect_questions.add(question)
        self.down_scores(scores)
        self.down_student_experience(scores)
        self.update_percentage_completed()
        self.save()
    
    def add_skipped_question(self,request, question):
        #Se a licao ja tiver sido concluida
        if not self.get_question(question):
            messages.success(request, TextMessage.LESSON_SUCCESS_COMPLETED)
            return
        
        #Se a questao ja tinha sido respondida corretamente antes
        if question in self.get_answered_correct_questions():
            messages.info(request, TextMessage.QUESTION_REPLY)
            return
        
        #Se a questao ja tinha sido saltada antes
        if question in self.get_skipped_questions():
            self.remove_skipped_question(question)
        
        
        #Se a questao ja tinha sido respondida incorretamente antes
        if question in self.get_answered_incorrect_questions():
            self.remove_answered_incorrect_questions(question)
        self.skipped_questions.add(question)
        self.save_skipped_question_historic(question)
        self.down_remaining_jump()
        self.save()
        if self.get_question(question) == question:
            messages.warning(request, TextMessage.QUESTION_IMPOSSIBLE_JUMP)
            return
        else:
            messages.success(request, TextMessage.QUESTION_SUCCESS_JUMP)
            return
    
    def remove_answered_incorrect_questions(self, question):
        self.answered_incorrect_questions.remove(question)
        self.save()
        
    
    def remove_skipped_question(self, question):
        self.skipped_questions.remove(question)
        self.save()
    
    def add_help_question(self, question):
        self.help_questions.add(question)
        self.save_help_question_historic(question)
        self.save()
        
    
                
        
    def answer_question(self, request, question, items):
        #Se a questao na pertence a essa licao
        if not question in self.lesson.get_questions():
            messages.error(request, TextMessage.QUESTION_NOT_FOUND_IN_LESSON)
            return
        
        #Se o items nao pertence a essa questao
        for item in items:
            exists = False
            for item_question in question.get_items():
                if item.id == item_question.id:
                    exists = True
            if not exists:
                messages.error(request, TextMessage.ITEM_NOT_FOUND_IN_QUESTION)
                return
        
        try:
            items_corrects = question.get_items_corrects()
        except Exception, e:
            print e
            messages.error(request, TextMessage.QUESTION_ERROR_REPLY)
            return
        
        if set(items_corrects) == set(items):
            self.add_answered_correct_question(question)
            self.save_answer_question_historic(question, items, True)
            messages.success(request, TextMessage.QUESTION_SUCCESS_REPLY)
            return
        else:
            self.add_answered_incorrect_question(question)
            self.save_answer_question_historic(question, items, False)
            messages.error(request, TextMessage.QUESTION_ERROR_REPLY)
            return
    
    def save_answer_question_historic(self, question, items, hit=False):
        try:
            student_historic = StudentHistoric.objects.get_or_create(student = self.student)[0]
        except:
            print "Erro save_answer_question"
            return
        try:
            print items
            answered_questions = AnsweredQuestionsHistoric(discipline=self.discipline, 
                                                           lesson = self.lesson,
                                                           question = question,
                                                           hit = hit)
            answered_questions.save()
            for item in items:
                answered_questions.items.add(item)
            student_historic.answered_questions_historic.add(answered_questions)
        except Exception, e:
            print e
            return
    def save_help_question_historic(self, question):
        try:
            student_historic = StudentHistoric.objects.get_or_create(student = self.student)[0]
        except Exception, e:
            print e
            return
        try:
            help_questions = HelpQuestionsHistoric(discipline=self.discipline, 
                                                           lesson = self.lesson,
                                                           question = question)
            help_questions.save()
            student_historic.help_questions_historic.add(help_questions)
        except  Exception, e:
            print e
            return
    def save_skipped_question_historic(self, question):
        try:
            student_historic = StudentHistoric.objects.get_or_create(student = self.student)[0]
        except Exception, e:
            print e
            return
        try:
            skipped_questions = SkippedQuestionsHistoric(discipline=self.discipline, 
                                                           lesson = self.lesson,
                                                           question = question)
            skipped_questions.save()
            student_historic.skipped_questions_historic.add(skipped_questions)
            student_historic.save()
        except Exception, e:
            print e
            return

    def up_student_experience(self, scores):
        from askmath.models import StudentExperience
        studentexperience = StudentExperience.objects.get_or_create(student = self.student, exists=True)[0]
        studentexperience.up_scores(scores)
            
    
    def down_student_experience(self, scores):
        from askmath.models import StudentExperience
        studentexperience = StudentExperience.objects.get_or_create(student = self.student, exists=True)[0]
        studentexperience.down_scores(scores)
    
    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()
        
    def update(self):
        self.update_percentage_completed()

    def __unicode__(self):
        return unicode(self.discipline) + ' - ' + unicode(self.lesson)
    
    class Meta:
        ordering = ['-discipline']
        verbose_name = _(u"Student Lesson State")
        verbose_name_plural = _(u"Students Lessons State")