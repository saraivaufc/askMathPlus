from askmath.entities import TextMessage
from askmath.models import Category as CategoryModel
from askmath.views.index import ProxyHome
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .category import Category
from .icategory import ICategory


class ProxyCategory(ICategory):
    def __init__(self):
        self.__category = Category()
        self.__proxy_home = ProxyHome()

    def view_categories(self, request):
        try:
            return self.__category.view_categories(request)
        except Exception, e:
            print e
            messages.error(request, TextMessage.ERROR)
            return self.__proxy_home.index(request)

    @method_decorator(login_required)
    def view_categories_removed(self, request):
        if request.user.has_perm("askmath.read_category") and request.user.has_perm("askmath.access_forum_admin"):
            try:
                return self.__category.view_categories_removed(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_categories(request)

    @method_decorator(login_required)
    def add_category(self, request):
        if request.user.has_perm("askmath.write_category") and request.user.has_perm("askmath.access_forum_admin"):
            try:
                return self.__category.add_category(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CATEGORY_ERROR_ADD)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_categories(request)

    @method_decorator(login_required)
    def remove_category(self, request, id_category):
        if request.user.has_perm("askmath.write_category") and request.user.has_perm("askmath.access_forum_admin"):
            try:
                category = CategoryModel.objects.get(id=id_category)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CATEGORY_NOT_FOUND)
                return self.view_categories(request)
            try:
                return self.__category.remove_category(request, category)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CATEGORY_ERROR_REM)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_categories(request)

    @method_decorator(login_required)
    def edit_category(self, request, id_category):
        if request.user.has_perm("askmath.write_category") and request.user.has_perm("askmath.access_forum_admin"):
            try:
                category = CategoryModel.objects.filter(id=id_category, exists=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.CATEGORY_NOT_FOUND)
                return self.view_category(request, id_category)
            try:
                return self.__category.edit_category(request, category)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CATEGORY_ERROR_EDIT)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_categories(request)

    @method_decorator(login_required)
    def restore_category(self, request, id_category):
        if request.user.has_perm("askmath.write_category") and request.user.has_perm("askmath.access_forum_admin"):
            try:
                category = CategoryModel.objects.get(id=id_category)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CATEGORY_NOT_FOUND)
                return self.view_category(request, id_category)
            try:
                return self.__category.restore_category(request, category)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CATEGORY_ERROR_RESTORE)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_categories(request)
