from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import Message, TextMessage, TypeMessage
from .icategory import ICategory
from .category import Category
from askmath.views.index import ProxyHome

class ProxyCategory(ICategory):
    def __init__(self):
        self.__category = Category()
        self.__proxy_home = ProxyHome()
        
    def view_categories(self, request, message=None):
        #try:
        return self.__category.view_categories(request, message)
        #except:
        #    message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        return self.__proxy_home.index(request, message)
    
    def view_categories_removed(self):
        pass
    
    def add_category(self):
        pass
    
    def remove_category(self):
        pass
    
    def edit_category(self):
        pass
    
    def restore_category(self):
        pass