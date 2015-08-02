from django.contrib import admin

from askmath.models.discipline import Discipline
from askmath.models.lesson import Lesson
from askmath.models.question import Question, Item
from askmath.models.users import Person, Administrator, Teacher, Assistant, Student, Contact
from askmath.models.video import Video
from askmath.models.progress import StudentQuestionProgress, StudentVideoProgress
from askmath.models.historic import StudentHistoric, AnsweredQuestionsHistoric, HelpQuestionsHistoric, SkippedQuestionsHistoric
from askmath.models.state import StudentLessonState
from askmath.models.experience import StudentExperience

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(Assistant)
class AssistantAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass

@admin.register(StudentQuestionProgress)
class StudentQuestionProgressAdmin(admin.ModelAdmin):
    pass

@admin.register(StudentVideoProgress)
class StudentVideoProgressAdmin(admin.ModelAdmin):
    pass

@admin.register(StudentHistoric)
class StudentHistoricAdmin(admin.ModelAdmin):
    pass

@admin.register(AnsweredQuestionsHistoric)
class AnsweredQuestionsHistoricAdmin(admin.ModelAdmin):
    pass

@admin.register(HelpQuestionsHistoric)
class HelpQuestionsHistoricAdmin(admin.ModelAdmin):
    pass


@admin.register(SkippedQuestionsHistoric)
class SkippedQuestionsHistoricAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentLessonState)
class StudentLessonStateAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentExperience)
class StudentExperienceAdmin(admin.ModelAdmin):
    pass
