#-*- encoding=UTF-8 -*- 

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models import Contact as ContactModel
from askmath.entities import TextMessage
from django.contrib import messages
from askmath.views.manager.contact.icontact import IContact
from django.utils.translation import ugettext_lazy as _

class Contact(IContact):
    
    def view_contacts(self, request):
        contacts = ContactModel.objects.filter(exists=True)
        return render(request, "askmath/manager/contact/manager_view_contacts.html",
            {'request':request,'contacts': contacts,'is_removed': False})
    
    def view_contacts_removed(self, request):
        contacts = ContactModel.objects.filter(exists=False)
        return render(request, "askmath/manager/contact/manager_view_contacts.html",
            {'request':request,'contacts': contacts,'is_removed': True})
        
    def view_contact(self, request,contact,message = None):
        return render(request, "askmath/manager/contact/manager_view_contact.html", 
            {'request':request,'contact': contact})
    
    def remove_contact(self, request,contact):
        contact.delete()
        messages.success(request, TextMessage.CONTACT_SUCCESS_REM)
        return self.view_contacts(request)
    
    def restore_contact(self, request,  contact):
        contact.restore()
        messages.error(request, TextMessage.CONTACT_SUCCESS_RESTORE)
        return self.view_contacts(request)