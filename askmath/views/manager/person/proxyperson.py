from askmath.entities import PersonTypes
from askmath.entities import TextMessage
from askmath.models.access import AdministratorKey, TeacherKey, AssistantKey
from askmath.models.users import Person as PersonModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from .iperson import IPerson
from .person import Person


class ProxyPerson(IPerson):
    def __init__(self):
        self.__account = Person()

    @method_decorator(login_required)
    def choose_person_types(self, request):
        if request.user.has_perm("askmath.read_person") and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__account.choose_person_types(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:home'))

    @method_decorator(login_required)
    def view_persons(self, request, PERSONTYPE):
        if request.user.has_perm("askmath.read_person") and request.user.has_perm("askmath.access_manager"):
            try:
                person_types = PersonTypes()
                if PERSONTYPE in person_types.get_types().keys():
                    return self.__account.view_persons(request, PERSONTYPE)
                else:
                    messages.error(request, TextMessage.ERROR)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR_GET_PARAMETERS)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_person_choose_person_types'))

    @method_decorator(login_required)
    def view_persons_removed(self, request, PERSONTYPE):
        if request.user.has_perm("askmath.read_person") and request.user.has_perm("askmath.access_manager"):
            try:
                person_types = PersonTypes()
                if PERSONTYPE in person_types.get_types():
                    return self.__account.view_persons_removed(request, PERSONTYPE)
                else:
                    messages.error(request, TextMessage.ERROR)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_person_view', kwargs={'PERSONTYPE': PERSONTYPE}))

    @method_decorator(login_required)
    def add_person(self, request, PERSONTYPE):
        if request.user.has_perm("askmath.write_person") and request.user.has_perm("askmath.access_manager"):
            try:
                person_types = PersonTypes()
                if PERSONTYPE in person_types.get_types():
                    return self.__account.add_person(request, PERSONTYPE)
            except Exception, e:
                print e
                messages.error(request, TextMessage.USER_ERROR_ADD)
                return HttpResponseRedirect(reverse('askmath:manager_person_view', kwargs={'PERSONTYPE': PERSONTYPE}))
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_person_view', kwargs={'PERSONTYPE': PERSONTYPE}))

    @method_decorator(login_required)
    def remove_person(self, request, PERSONTYPE, id_person):
        if request.user.has_perm("askmath.write_person") and request.user.has_perm("askmath.access_manager"):
            try:
                person_types = PersonTypes()
                if PERSONTYPE in person_types.get_types():
                    person = PersonModel.objects.get(id=id_person)
            except Exception, e:
                print e
                messages.error(request, TextMessage.USER_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_person_view', kwargs={'PERSONTYPE': PERSONTYPE}))
            try:
                return self.__account.remove_person(request, PERSONTYPE, person)
            except Exception, e:
                print e
                messages.error(request, TextMessage.USER_ERROR_REM)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_person_view', kwargs={'PERSONTYPE': PERSONTYPE}))

    @method_decorator(login_required)
    def remove_registerkey(self, request, PERSONTYPE, id_registerkey):
        if request.user.has_perm("askmath.write_person") and request.user.has_perm("askmath.access_manager"):
            try:
                person_types = PersonTypes()
                if PERSONTYPE in person_types.get_types():
                    person_types = PersonTypes(PERSONTYPE)
                    if PERSONTYPE == person_types.ADMIN:
                        registerkey = AdministratorKey.objects.get(id=id_registerkey)
                    elif PERSONTYPE == person_types.TEACHER:
                        registerkey = TeacherKey.objects.get(id=id_registerkey)
                    elif PERSONTYPE == person_types.ASSISTANT:
                        registerkey = AssistantKey.objects.get(id=id_registerkey)
                    else:
                        registerkey = False
            except Exception, e:
                print e
                messages.error(request, TextMessage.USER_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_person_view', kwargs={'PERSONTYPE': PERSONTYPE}))
            try:
                return self.__account.remove_registerkey(request, PERSONTYPE, registerkey)
            except Exception, e:
                print e
                messages.error(request, TextMessage.USER_ERROR_REM)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_person_view', kwargs={'PERSONTYPE': PERSONTYPE}))

    @method_decorator(login_required)
    def restore_person(self, request, PERSONTYPE, id_person):
        if request.user.has_perm("askmath.write_person") and request.user.has_perm("askmath.access_manager"):
            try:
                person_types = PersonTypes()
                if PERSONTYPE in person_types.get_types():
                    person = PersonModel.objects.get(id=id_person)
            except Exception, e:
                print e
                messages.error(request, TextMessage.USER_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_person_view', kwargs={'PERSONTYPE': PERSONTYPE}))
            try:
                return self.__account.restore_person(request, PERSONTYPE, person)
            except Exception, e:
                print e
                messages.error(request, TextMessage.USER_ERROR_RESTORE)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return HttpResponseRedirect(reverse('askmath:manager_person_view', kwargs={'PERSONTYPE': PERSONTYPE}))