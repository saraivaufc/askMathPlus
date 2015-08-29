from .icategory import ICategory
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models import Category as CategoryModel
from askmath.entities import Message, TextMessage, TypeMessage
from askmath.forms import CategoryForm, TopicForm
from django.utils.translation import ugettext_lazy as _

class Category(ICategory):
    def view_categories(self, request, message=None):
        categories = CategoryModel.objects.filter(exists=True)
        return render(request, "askmath/manager/forum/category/manager_view_categories.html",
            {'request':request,'categories': categories,'message': message})
    
    def view_categories_removed(self, request, message=None):
        categories = CategoryModel.objects.filter(exists=False)
        return render(request, "askmath/manager/forum/category/manager_view_categories.html",
            {'request':request,'categories': categories, 'is_removed':True ,'message': message})
    
    def view_category(self, request, category, message=None):
        form_topic = TopicForm()
        topics = category.get_topics()
        return render(request, "askmath/manager/forum/category/manager_view_category.html", 
            {'request':request,'category': category,'topics':topics,'form_topic': form_topic ,'message': message})
    
    def view_category_removed(self, request, category, message=None):
        topics = category.get_topics_removed()
        return render(request, "askmath/manager/forum/category/manager_view_category.html", 
            {'request':request,'category': category,'topics':topics, 'message': message})
    
    def add_category(self, request, message=None):
        if request.method == "POST":
            request.POST = request.POST.copy()
            request.POST['person'] = request.user.id
            print request.POST
            form = CategoryForm(request.POST)
            if form.is_valid():
                category = form.save()
                message = Message(TextMessage.CATEGORY_SUCCESS_ADD, TypeMessage.SUCCESS)
                return self.view_categories(request, message)
                
        else:
            form = CategoryForm()
        return render(request, "askmath/manager/forum/category/manager_form_category.html", 
            {'request':request,'form': form, 'title_form':_('Create Category'), 'message': message})
    
    def remove_category(self, request, category, message=None):
        category.delete()
        message = Message(TextMessage.CATEGORY_SUCCESS_REM, TypeMessage.SUCCESS)
        return self.view_categories(request, message)
    
    def edit_category(self, request, category, message=None):
        if request.method == 'POST':
            request.POST = request.POST.copy()
            request.POST['person'] = request.user.id
            form = CategoryForm(request.POST, instance = category)
            if form.is_valid():
                category=form.save()
                message = Message(TextMessage.CATEGORY_SUCCESS_EDIT, TypeMessage.SUCCESS)
                return self.view_category(request, category, message)
            else:
                message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
                
        else:
            form = CategoryForm( instance = category)
        return render(request, "askmath/manager/forum/category/manager_form_category.html", 
            {'request':request,'form': form,'category': category, 'title_form':_('Edit Category'), 'message': message})
    
    
    def restore_category(self, request, category, message=None):
        category.restore()
        message = Message(TextMessage.CATEGORY_SUCCESS_RESTORE, TypeMessage.SUCCESS)
        return self.view_categories(request, message)