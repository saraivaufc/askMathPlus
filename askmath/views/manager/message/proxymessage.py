#-*- encoding=UTF-8 -*- 

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import TextMessage
from django.contrib import messages
from askmath.views.index import ProxyHome
from askmath.models import Message as MessageModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .imessage import IMessage
from .message import Message

class ProxyMessage(IMessage):
    
    def __init__(self):
        self.__message = Message()
        self.__proxy_home = ProxyHome()
  
    @method_decorator(login_required)
    def view_messages(self, request):
        if request.user.has_perm("askmath.read_message")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__message.view_messages(request)
            except Exception,e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.__proxy_home.index(request)
    
    @method_decorator(login_required)
    def view_messages_removed(self,request):
        if request.user.has_perm("askmath.read_message")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__message.view_messages_removed(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_messages(request)
    
    @method_decorator(login_required)
    def view_message(self, request, id_message):
        if request.user.has_perm("askmath.read_message")  and request.user.has_perm("askmath.access_manager"):
            try:
                message_model = MessageModel.objects.get(id = id_message)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CONTACT_NOT_FOUND)
                return self.view_messages(request)
            try:
                return self.__message.view_message(request, message_model)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_messages(request)
    
    @method_decorator(login_required)
    def remove_message(self, request, id_message):
        if request.user.has_perm("askmath.write_message")  and request.user.has_perm("askmath.access_manager"):
            try:
                message = MessageModel.objects.get(id = id_message)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CONTACT_NOT_FOUND)
                return self.view_messages(request)
            try:
                return self.__message.remove_message(request,message)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CONTACT_ERROR_REM)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_messages(request)
    
    @method_decorator(login_required)
    def restore_message(self, request, id_message=None):
        if request.user.has_perm("askmath.write_message")  and request.user.has_perm("askmath.access_manager"):
            try:
                message = MessageModel.objects.get(id = id_message)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CONTACT_NOT_FOUND)
                return self.view_messages(request)
            try:
                return self.__message.restore_message(request, message)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CONTACT_ERROR_RESTORE)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_messages(request)