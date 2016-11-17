from askmath.models import Lesson

class LessonSorting():
	"""
	Class for ordering the lessons using topological sorting.
	"""
	def __init__(self, initial_lessons):
		"""
		This function takes as a parameter a list of lessons that do not have prerequisites.
		"""
		self.__lessons = list(initial_lessons)
		self.__lessons_levels = {}
		self.__lessons_in_levels = []

	def get_result(self):
		level = 0
		while self.__lessons:
			temp_lessons_level = []
			temp_lessons_in_levels = []
			for index, l in enumerate(self.__lessons):
				if not l in self.__lessons_in_levels:
					insert = True
					for r in l.get_requirements():
						if not r in self.__lessons_in_levels:
							insert=False
					if insert:
						temp_lessons_level.append(l)
						temp_lessons_in_levels.append(l)
						self.__lessons.pop(index)
			self.__lessons_levels[level] = temp_lessons_level
			self.__lessons_in_levels.extend(temp_lessons_level)
			level +=1
		return self.__lessons_levels






