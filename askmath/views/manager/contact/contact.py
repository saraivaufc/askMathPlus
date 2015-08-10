#-*- encoding=UTF-8 -*- 

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models import Contact as ContactModel
from askmath.entities import Message, TextMessage, TypeMessage
from askmath.views.manager.contact.icontact import IContact
from askMathPlus.settings import COLORS_ALL
from django.utils.translation import ugettext_lazy as _

class Contact(IContact):
    
    def view_contacts(self, request, message = None):
        contacts = ContactModel.objects.filter(exists=True)
        return render(request, "askmath/manager/contact/manager_view_contacts.html",
            {'request':request,'contacts': contacts,'is_removed': False,'colors': COLORS_ALL, 'message': message})
    
    def view_contacts_removed(self, request, message = None):
        contacts = ContactModel.objects.filter(exists=False)
        return render(request, "askmath/manager/contact/manager_view_contacts.html",
            {'request':request,'contacts': contacts,'is_removed': True,'colors': COLORS_ALL, 'message': message})
        
    def view_contact(self, request,contact,message = None):
        return render(request, "askmath/manager/contact/manager_view_contact.html", 
            {'request':request,'contact': contact ,'message': message, 'colors': COLORS_ALL })
    
    def remove_contact(self, request,contact, message = None):
        contact.delete()
        message = Message(TextMessage.CONTACT_SUCCESS_REM, TypeMessage.SUCCESS)
        return self.view_contacts(request, message)
    
    def restore_contact(self, request,  contact):
        contact.restore()
        message = Message(TextMessage.CONTACT_SUCCESS_RESTORE, TypeMessage.SUCCESS)
        return self.view_contacts(request, message)