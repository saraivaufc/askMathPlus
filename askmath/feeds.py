from django.contrib.syndication.views import Feed
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from askmath.models.lesson import Lesson

class LessonsLatests(Feed):
	title = _('AskMath')
	link = '/askmath/'
	description = _("The AskMath is reported here!")

	def items(self):
		return Lesson.objects.filter(exists=True, visible=True).order_by('-creation')[:10]

	def item_title(self, lesson):
		try:
			discipline = lesson.get_disciplines(visible=True)[0]
		except:
			discipline = None
		if discipline:
			return discipline.get_title() + " >> " + lesson.get_title()
		else:
			return lesson.get_title()

	def item_description(self, item):
		return item.description

	# item_link is only needed if NewsItem has no get_absolute_url method.
	def item_link(self, item):
		return reverse('lesson-item', args=[item.pk])

	def items(self):
		return Lesson.objects.filter(exists=True, visible=True).order_by('-creation')

	def item_link(self, lesson):
		try:
			discipline = lesson.get_disciplines(visible=True)[0]
		except:
			discipline = 0
		return '/contents/lesson=%d/' %(lesson.id)