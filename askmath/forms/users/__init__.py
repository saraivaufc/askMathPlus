from administrator import AdministratorForm
from assistant import AssistantForm
from person import RegisterForm, ProfileForm, LoginForm,RecoverPassword, AlterPassword
from student import StudentForm
from teacher import TeacherForm
from message import MessageForm, MessageFormRecaptcha


__all__ = [
    'RegisterForm','ProfileForm', 'LoginForm' ,'RecoverPassword','AlterPassword' ,'MessageForm','MessageFormRecaptcha','AdministratorForm', 'TeacherForm', 'AssistantForm', 'StudentForm', 
]
