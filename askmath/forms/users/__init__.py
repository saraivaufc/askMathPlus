from administrator import AdministratorForm
from assistant import AssistantForm
from person import PersonForm, PersonProfile, PersonLoginForm,PersonRecoverPassword, PersonAlterPassword
from student import StudentForm
from teacher import TeacherForm
from message import MessageForm


__all__ = [
    'PersonForm','PersonProfile', 'PersonLoginForm' ,'PersonRecoverPassword','PersonAlterPassword' ,'MessageForm','AdministratorForm', 'TeacherForm', 'AssistantForm', 'StudentForm', 
]
