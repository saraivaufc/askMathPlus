from askmath.models.access import AdministratorKey, TeacherKey, AssistantKey
from askmath.models.category import Category
from askmath.models.comment import Comment
from askmath.models.discipline import Discipline
from askmath.models.experience import StudentExperience
from askmath.models.historic import StudentHistoric, AnsweredQuestionsHistoric, HelpQuestionsHistoric, \
	SkippedQuestionsHistoric
from askmath.models.lesson import Lesson
from askmath.models.like import Like
from askmath.models.progress import StudentQuestionProgress, StudentVideoProgress
from askmath.models.question import Question, Item
from askmath.models.state import StudentLessonState
from askmath.models.topic import Topic
from askmath.models.users import Person, Administrator, Teacher, Assistant, Student, Message
from askmath.models.video import Video
from django.contrib import admin


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
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
	list_filter = ('discipline', )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('lesson', 'description')
	list_filter = ('lesson', )


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
	list_display = ('student', 'discipline', 'lesson', 'exists', 'percentage_completed')
	list_filter = ('student', 'discipline', 'lesson', 'exists')

@admin.register(StudentExperience)
class StudentExperienceAdmin(admin.ModelAdmin):
	pass


@admin.register(AdministratorKey)
class AdministratorKeyAdmin(admin.ModelAdmin):
	pass


@admin.register(TeacherKey)
class TeacherKeyAdmin(admin.ModelAdmin):
	pass


@admin.register(AssistantKey)
class AssistantKeyAdmin(admin.ModelAdmin):
	pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
	pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
	pass
