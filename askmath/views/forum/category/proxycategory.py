from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import Message, TextMessage, TypeMessage
from askmath.views.index import ProxyHome
from askmath.models import Category as CategoryModel
from .icategory import ICategory
from .category import Category
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ProxyCategory(ICategory):
    def __init__(self):
        self.__category = Category()
        self.__proxy_home = ProxyHome()
    
    @method_decorator(login_required)
    def view_categories(self, request, message=None):
        if request.user.has_perm("askmath.read_category"):
            try:
                return self.__category.view_categories(request, message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__proxy_home.index(request, message)
    
    @method_decorator(login_required)
    def view_categories_removed(self, request, message=None):
        if request.user.has_perm("askmath.read_category")  and request.user.has_perm("askmath.access_forum_admin"):
            try:
                return self.__category.view_categories_removed(request, message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_categories(request, message)
    
    @method_decorator(login_required)
    def view_category(self, request, id_category, message=None):
        if request.user.has_perm("askmath.read_category"):
            try:
                category = CategoryModel.objects.get(id = id_category)
            except:
                message = Message(TextMessage.CATEGORY_NOT_FOUND, TypeMessage.ERROR)
                return self.view_categories(request, message)
            try:
                return self.__category.view_category(request, category, message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_categories(request, message)
    
    @method_decorator(login_required)
    def view_category_removed(self, request, id_category, message=None):
        if request.user.has_perm("askmath.read_category")  and request.user.has_perm("askmath.access_forum_admin"):
            try:
                category = CategoryModel.objects.get(id = id_category)
            except:
                message = Message(TextMessage.CATEGORY_NOT_FOUND, TypeMessage.ERROR)
                return self.view_categories(request, message)
            try:
                return self.__category.view_category_removed(request, category)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_categories(request, message)
    @method_decorator(login_required)
    def add_category(self, request, message=None):
        if request.user.has_perm("askmath.write_category")  and request.user.has_perm("askmath.access_forum_admin"):
            try:
                return self.__category.add_category(request, message)
            except:
                message = Message(TextMessage.CATEGORY_ERROR_ADD, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_categories(request, message)
    
    @method_decorator(login_required)
    def remove_category(self, request, id_category, message=None):
        if request.user.has_perm("askmath.write_category")  and request.user.has_perm("askmath.access_forum_admin"):
            try:
                category = CategoryModel.objects.get(id = id_category)
            except:
                message = Message(TextMessage.CATEGORY_NOT_FOUND, TypeMessage.ERROR)
                return self.view_categories(request, message)
            try:
                return self.__category.remove_category(request, category, message)
            except:
                message = Message(TextMessage.CATEGORY_ERROR_REM, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_categories(request, message)
    
    @method_decorator(login_required)
    def edit_category(self, request, id_category, message=None):
        if request.user.has_perm("askmath.write_category")  and request.user.has_perm("askmath.access_forum_admin"):
            try:
                category = CategoryModel.objects.filter(id = id_category, exists=True)[0]
            except:
                message = Message(TextMessage.CATEGORY_NOT_FOUND, TypeMessage.ERROR)
                return self.view_category(request, id_category, message)
            try:
                return self.__category.edit_category(request, category, message)
            except:
                message = Message(TextMessage.CATEGORY_ERROR_EDIT, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_categories(request, message)
    
    @method_decorator(login_required)
    def restore_category(self, request, id_category, message=None):
        if request.user.has_perm("askmath.write_category")  and request.user.has_perm("askmath.access_forum_admin"):
            try:
                category = CategoryModel.objects.get(id = id_category)
            except:
                message = Message(TextMessage.CATEGORY_NOT_FOUND, TypeMessage.ERROR)
                return self.view_category(request, id_category, message)
            try:
                return self.__category.restore_category(request, category, message)
            except:
                message = Message(TextMessage.CATEGORY_ERROR_RESTORE, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_categories(request, message)