from .icategory import ICategory
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models import Category as CategoryModel
from askmath.entities import TextMessage
from django.contrib import messages
from askmath.forms import CategoryForm, TopicForm
from django.utils.translation import ugettext_lazy as _

class Category(ICategory):
    def view_categories(self, request):
        categories = CategoryModel.objects.filter(exists=True)
        return render(request, "askmath/forum/category/view_categories.html",
            {'request':request,'categories': categories})
    
    def view_categories_removed(self, request):
        categories = CategoryModel.objects.filter(exists=False)
        return render(request, "askmath/forum/category/view_categories.html",
            {'request':request,'categories': categories, 'is_removed':True})
    
    def view_category(self, request, category):
        form_topic = TopicForm()
        topics = category.get_topics()
        return render(request, "askmath/forum/category/view_category.html", 
            {'request':request,'category': category,'topics':topics,'form_topic': form_topic})
    
    def view_category_removed(self, request, category):
        topics = category.get_topics_removed()
        return render(request, "askmath/forum/category/view_category.html", 
            {'request':request,'category': category,'topics':topics})
    
    def add_category(self, request):
        if request.method == "POST":
            request.POST = request.POST.copy()
            request.POST['person'] = request.user.id
            print request.POST
            form = CategoryForm(request.POST)
            if form.is_valid():
                category = form.save()
                messages.success(request, TextMessage.CATEGORY_SUCCESS_ADD)
                return self.view_categories(request)
            else:
                messages.error(request, TextMessage.ERROR_FORM)
        else:
            form = CategoryForm()
        return render(request, "askmath/forum/category/form_category.html", 
            {'request':request,'form': form, 'title_form':_('Create Category')})
    
    def remove_category(self, request, category):
        category.delete()
        messages.success(request, TextMessage.CATEGORY_SUCCESS_REM)
        return self.view_categories(request)
    
    def edit_category(self, request, category):
        if request.method == 'POST':
            request.POST = request.POST.copy()
            request.POST['person'] = request.user.id
            form = CategoryForm(request.POST, instance = category)
            if form.is_valid():
                category=form.save()
                messages.success(request, TextMessage.CATEGORY_SUCCESS_ADD)
                return self.view_category(request, category)
            else:
                messages.error(request, TextMessage.ERROR_FORM)
                
        else:
            form = CategoryForm( instance = category)
        return render(request, "askmath/forum/category/form_category.html", 
            {'request':request,'form': form,'category': category, 'title_form':_('Edit Category')})
    
    
    def restore_category(self, request, category):
        category.restore()
        messages.success(request, TextMessage.CATEGORY_SUCCESS_RESTORE)
        return self.view_categories(request)