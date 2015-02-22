
from django.contrib.auth.models import AbstractUser
from spirit.models.user import AbstractForumUser


class User(AbstractUser, AbstractForumUser):
	class Meta:
		db_table = 'auth_user'


from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^spirit\.utils\.models\.AutoSlugField"])