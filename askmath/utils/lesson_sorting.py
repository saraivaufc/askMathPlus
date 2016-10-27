from askmath.models import Lesson

class LessonSorting():
	"""
	Class for ordering the lessons using topological sorting.
	"""
	def __init__(self, initial_lessons, discipline_filter):
		"""
		This function takes as a parameter a list of lessons that do not have prerequisites.
		"""
		self.__lesson_no_edges = initial_lessons
		self.__lessons_ordered = []
		self.__visited_nodes = []
		self.__discipline_filter = discipline_filter

	def visit(self, lesson):
		if not lesson.id in self.__visited_nodes:
			self.__visited_nodes.append(lesson.id)
			for l in Lesson.objects.filter(requirements=lesson.id, discipline = self.__discipline_filter.id, exists=True, visible=True):
				self.visit(l)
			self.__lessons_ordered.insert(0, lesson)

	def get_result(self):
		for i in self.__lesson_no_edges:
			self.visit(i)
		return self.__lessons_ordered




