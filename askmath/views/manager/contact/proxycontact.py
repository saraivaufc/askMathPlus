#-*- encoding=UTF-8 -*- 

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import TextMessage
from django.contrib import messages
from askmath.views.index import ProxyHome
from askmath.models import Contact as ContactModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .icontact import IContact
from .contact import Contact

class ProxyContact(IContact):
    
    def __init__(self):
        self.__contact = Contact()
        self.__proxy_home = ProxyHome()
  
    @method_decorator(login_required)
    def view_contacts(self, request):
        if request.user.has_perm("askmath.read_contact")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__contact.view_contacts(request)
            except Exception,e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.__proxy_home.index(request)
    
    @method_decorator(login_required)
    def view_contacts_removed(self,request):
        if request.user.has_perm("askmath.read_contact")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__contact.view_contacts_removed(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_contacts(request)
    
    @method_decorator(login_required)
    def view_contact(self, request, id_contact):
        if request.user.has_perm("askmath.read_contact")  and request.user.has_perm("askmath.access_manager"):
            try:
                contact = ContactModel.objects.get(id = id_contact)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CONTACT_NOT_FOUND)
                return self.view_contacts(request)
            try:
                return self.__contact.view_contact(request, contact)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_contacts(request)
    
    @method_decorator(login_required)
    def remove_contact(self, request, id_contact):
        if request.user.has_perm("askmath.write_contact")  and request.user.has_perm("askmath.access_manager"):
            try:
                contact = ContactModel.objects.get(id = id_contact)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CONTACT_NOT_FOUND)
                return self.view_contacts(request)
            try:
                return self.__contact.remove_contact(request,contact)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CONTACT_ERROR_REM)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_contacts(request)
    
    @method_decorator(login_required)
    def restore_contact(self, request, id_contact=None):
        if request.user.has_perm("askmath.write_contact")  and request.user.has_perm("askmath.access_manager"):
            try:
                contact = ContactModel.objects.get(id = id_contact)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CONTACT_NOT_FOUND)
                return self.view_contacts(request)
            try:
                return self.__contact.restore_contact(request, contact)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CONTACT_ERROR_RESTORE)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_contacts(request)