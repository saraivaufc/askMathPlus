#-*- encoding=UTF-8 -*- 

from askmath.entities import TextMessage
from askmath.models import Message as MessageModel
from askmath.views.manager.message.imessage import IMessage
from django.contrib import messages
from django.shortcuts import render


class Message(IMessage):
    
    def view_messages(self, request):
        messages_model = MessageModel.objects.filter(exists=True)
        return render(request, "askmath/manager/message/manager_view_messages.html",
            {'request':request,'messages_model': messages_model,'is_removed': False})
    
    def view_messages_removed(self, request):
        messages_model = MessageModel.objects.filter(exists=False)
        return render(request, "askmath/manager/message/manager_view_messages.html",
            {'request':request,'messages_model': messages_model,'is_removed': True})
        
    def remove_message(self, request,message_model):
        message_model.delete()
        messages.success(request, TextMessage.MESSAGE_SUCCESS_REM)
        return self.view_messages(request)
    
    def restore_message(self, request,  message_model):
        message_model.restore()
        messages.success(request, TextMessage.MESSAGE_SUCCESS_RESTORE)
        return self.view_messages(request)