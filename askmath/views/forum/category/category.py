from .icategory import ICategory
from django.shortcuts import render
from askmath.models.category import Category as CategoryModel
class Category(ICategory):
    def view_categories(self, request, message=None):
        categories = CategoryModel.objects.filter(exists=True)
        return render(request, 'askmath/forum/category/forum_view_categories.html',
            {'request': request,'categories': categories ,'message': message})
    
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