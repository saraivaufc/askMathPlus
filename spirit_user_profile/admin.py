from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _

from .models import User


class CustomUserAdmin(UserAdmin):
    # You can use UserAdmin directly, this subclass adds administrator and moderator fields.
    # If you are a superuser, just save your user in the admin and it'll automatically become an administrator.
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'is_administrator', 'is_moderator',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, CustomUserAdmin)