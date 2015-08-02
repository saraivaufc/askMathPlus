from askmath.models import StudentHistoric, Lesson, Question

class GeneratorStatistics():
    #STATISTICS
    def get_acerts_question(self, question):
        answered_dict = {}
        for student_historic in StudentHistoric.objects.all():
            student = student_historic.get_student()
            answered_dict[student.get_username()]= student_historic.get_answered_questions_historic()
        print answered_dict.keys()
        answered_values = {}
        for student, answered_questions in answered_dict.items():
            for answered_question in answered_questions:
                if answered_question.get_hit() and answered_question.get_question().id == question.id:
                    answered_values[student] = 1
                    break
        
        answered_list = answered_values.values()
        print answered_list
        try:
            value = sum(answered_list)
        except ZeroDivisionError:
            value=0
        return value
    
    def get_errors_question(self, question):
        answered_dict = {}
        for student_historic in StudentHistoric.objects.all():
            student = student_historic.get_student()
            answered_dict[student.get_username()]= student_historic.get_answered_questions_historic()
        print answered_dict.keys()
        answered_values = {}
        for student, answered_questions in answered_dict.items():
            for answered_question in answered_questions:
                if answered_question.get_hit() == False  and answered_question.get_question().id == question.id:
                    answered_values[student] = 1
                    break
        
        answered_list = answered_values.values()
        print answered_list
        try:
            value = sum(answered_list)
        except ZeroDivisionError:
            value=0
        return value
    
    def get_skippeds_question(self, question):
        skipped_dict = {}
        for student_historic in StudentHistoric.objects.all():
            student = student_historic.get_student()
            skipped_dict[student.get_username()]= student_historic.get_skipped_questions_historic()
        skipped_values = {}
        for student, skipperd_questions in skipped_dict.items():
            for skipperd_question in skipperd_questions:
                if skipperd_question.get_question().id == question.id:
                    try:
                        skipped_values[student]
                    except:
                        skipped_values[student] = 0
                    skipped_values[student]+=1
                    break
        
        skipped_list = skipped_values.values()
        print skipped_list
        try:
            value = sum(skipped_list)
        except ZeroDivisionError:
            value=0
        return value
    
    def get_helps_question(self, question):
        help_dict = {}
        for student_historic in StudentHistoric.objects.all():
            student = student_historic.get_student()
            help_dict[student.get_username()]= student_historic.get_help_questions_historic()
        help_values = {}
        for student, help_questions in help_dict.items():
            for help_question in help_questions:
                if help_question.get_question().id == question.id:
                    try:
                        help_values[student]
                    except:
                        help_values[student] = 0
                    help_values[student]+=1
                    break
        
        help_list = help_values.values()
        print help_list
        try:
            value = sum(help_list)
        except ZeroDivisionError:
            value=0
        return value
    
    
    def get_percentage_answered_questions(self, lesson):
        acerts = 0
        errors = 0
        skippeds = 0
        helps = 0
        for i in lesson.get_questions():
            acerts+=self.get_acerts_question(i)
            errors+=self.get_errors_question(i)
            skippeds += self.get_skippeds_question(i)
            helps += self.get_helps_question(i)
        total = float(acerts + errors + skippeds + helps)
        try:
            acerts = (acerts * 100)/total
        except ZeroDivisionError:
            acerts = 0
        try:
            errors = (errors * 100)/total
        except ZeroDivisionError:
            errors = 0
        try:
            skippeds = (skippeds * 100)/total
        except ZeroDivisionError:
            skippeds = 0
        try:
            helps = (helps * 100)/total
        except ZeroDivisionError:
            helps = 0
            
        return {'Acerts':acerts, 'Errors':errors, 'Skippeds': skippeds, 'Helps':helps}