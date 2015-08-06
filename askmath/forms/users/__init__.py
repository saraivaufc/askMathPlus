from administrator import AdministratorForm
from assistant import AssistantForm
from person import PersonForm, PersonProfile, PersonLoginForm,PersonRecoverPassword, PersonAlterPassword
from student import StudentForm
from teacher import TeacherForm
from contact import ContactForm


__all__ = [
    'PersonForm','PersonProfile', 'PersonLoginForm' ,'PersonRecoverPassword','PersonAlterPassword' ,'ContactForm','AdministratorForm', 'TeacherForm', 'AssistantForm', 'StudentForm', 
]
