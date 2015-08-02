#-*- encoding=UTF-8 -*-

from django.utils.translation import ugettext as _


class TypeMessage():
	SUCCESS = _('SUCCESS')
	INFO = _('INFO')
	WARNING = _('WARNING')
	ERROR = _('ERROR')

class TextMessage():
	
	#User
	USER_NOT_PERMISSION = _("User does not have permission.")
	USER_NOT_FOUND = _("User not found.")
	USER_PASSWORD_ERRRO = _("Incorrect password.")
	USER_IS_AUTHENTICATED = _("User is authenticated.")
	USER_NOT_AUTHENTICATED = _("User is not authenticated.")
	USER_CREATED_SUCCESS = _("User created successfully.")
	USER_CREATED_ERROR = _("Failed to create user.")
	USER_ADD_GROUP_ERROR = _("Failed to add group.")
	
	EMAIL_RECOVER_PASSWORD_SUCCESS = _("Email of recover password send success.")
	EMAIL_RECOVER_PASSWORD_ERROR = _("Email of recover password send error.")


	#Login and Logout
	LOGIN_SUCCESS = _("Login successfully performed..") 
	LOGIN_ERROR = _("Failed to perform login.") 
	LOGOUT_SUCCESS = _("Logout successfully performed.")
	LOGOUT_ERROR = _("Failed to perform logout.")

	#Requests
	POST_REQUIRED = _("POST required.")

	ERROR = _("Error, Contact Administrator.")

	#Forms
	ERROR_FORM = _("There was an error on the form.")


	#Discipline
	DISCIPLINE_SUCCESS_ADD = _("Discipline successfully added.")
	DISCIPLINE_ERROR_ADD = _("Error adding discipline.")
 	
	DISCIPLINE_SUCCESS_EDIT = _("Discipline successfully edit.")
	DISCIPLINE_ERROR_EDIT = _("Error edit discipline.")
 	
	DISCIPLINE_SUCCESS_REM = _("Discipline successfully removed.")
	DISCIPLINE_ERROR_REM = _("Error remove discipline.")
	
	DISCIPLINE_SUCCESS_RESTORE = _("Discipline successfully restored.")
	DISCIPLINE_ERROR_RESTORE = _("Error restore discipline.")
 
	DISCIPLINE_NOT_FOUND = _("Discipline not found.")

	#Lesson
 	LESSON_SUCCESS_ADD = _("Lesson successfully added.")
 	LESSON_ERROR_ADD = _("Error adding lesson.")
 	
 	LESSON_SUCCESS_EDIT = _("Lesson successfully edit.")
 	LESSON_ERROR_EDIT = _("Error edit lesson.")
 	
 	LESSON_SUCCESS_REM = _("Lesson successfully removed.")
 	LESSON_ERROR_REM = _("Error remove lesson.")
 	
 	LESSON_SUCCESS_RESTORE = _("Lesson successfully restored.")
	LESSON_ERROR_RESTORE = _("Error restore lesson.")
 
 	LESSON_NOT_FOUND = _("Lesson not found.")
 	LESSON_SUCCESS_COMPLETED = _("Lesson successfully completed.")
 	
 	LESSON_SUCCESS_RESET = _("Lesson successfully reset.")
 	
 	LESSON_NOT_REMAINING_JUMPS = _("Lesson not remaining jumps.")
 	
 	#Question
 	QUESTION_SUCCESS_ADD = _("Question successfully added.")
 	QUESTION_ERROR_ADD = _("Error adding question.")
 	
 	QUESTION_SUCCESS_EDIT = _("Question successfully edit.")
 	QUESTION_ERROR_EDIT = _("Error edit question.")
 	
 	QUESTION_SUCCESS_REM = _("Question successfully removed.")
 	QUESTION_ERROR_REM = _("Error remove question.")
 	
 	QUESTION_SUCCESS_RESTORE = _("Question successfully restored.")
	QUESTION_ERROR_RESTORE = _("Error restore question.")
	
	QUESTION_SUCCESS_SORT = _("Question successfully sorted.")
	QUESTION_ERROR_SORT = _("Error sorted question.")
 
 	QUESTION_NOT_FOUND = _("Question not found.")
 	
 	QUESTION_SUCCESS_REPLY = _("Your reply is correct.")
 	QUESTION_ERROR_REPLY = _("Your reply is incorrect.")
 	QUESTION_REPLY = _("Question is reply.")
 	
 	QUESTION_SUCCESS_JUMP = _("Jump realization with successfully.")
 	QUESTION_JUMP = _("Question is jump.")
 	QUESTION_ERROR_JUMP = _("Question error in jump.")
 	
 	QUESTION_NOT_FOUND_IN_LESSON = _("Question not found in lesson.")
 	
 	#Item
 	ITEM_NOT_FOUND = _("Item not found.")
 	ITEM_NOT_FOUND_IN_QUESTION = _("Item not found in question.")
 	
	#Video
 	VIDEO_SUCCESS_ADD = _("Video successfully added.")
 	VIDEO_ERROR_ADD = _("Error adding video.")
 	
 	VIDEO_SUCCESS_EDIT = _("Video successfully edit.")
 	VIDEO_ERROR_EDIT = _("Error edit video.")
 	
 	VIDEO_SUCCESS_REM = _("Video successfully removed.")
 	VIDEO_ERROR_REM = _("Error remove video.")
 	
 	VIDEO_SUCCESS_RESTORE = _("Video successfully restored.")
	VIDEO_ERROR_RESTORE = _("Error restore video.")
	
	VIDEO_SUCCESS_SORT = _("Video successfully sorted.")
	VIDEO_ERROR_SORT = _("Error sorted video.")
 
 	VIDEO_NOT_FOUND = _("Video not found.")
 	VIDEO_NOT_FOUND_IN_LESSON = _("Video not found in lesson.")
 	
 	
 	

	
	#Person
 	PERSON_SUCCESS_ADD = _("Person successfully added.")
 	PERSON_ERROR_ADD = _("Error adding person.")
 	
 	PERSON_SUCCESS_EDIT = _("Person successfully edit.")
 	PERSON_ERROR_EDIT = _("Error edit person.")
 	
 	PERSON_SUCCESS_REM = _("Person successfully removed.")
 	PERSON_ERROR_REM = _("Error remove person.")
 	
 	PERSON_SUCCESS_RESTORE = _("Person successfully restored.")
	PERSON_ERROR_RESTORE = _("Error restore person.")
 
 	PERSON_NOT_FOUND = _("Person not found.")
 	
 	#Statistics
 	
 	STATISTIC_NOT_FOUND = _("Statistic not found.")



	#Parameters
	ERROR_GET_PARAMETERS = _("Error pick up the parameters.")
	
	#Results
	NO_RESULTS_FOUND  = _("No results found.")
	
	#Request
	METHOD_NOT_POST  = _("Method not is POST.")
	METHOD_NOT_GET  = _("Method not is GET.")

	#Messages
	MESSAGE_SUCCESS_SEND = _("Message successfully send.")
	



class Message():
	text = ''
	type_msg =None 
	def __init__(self, text, type_msg):
		self.text = str(text)
		self.type_msg = type_msg

	def type(self):
		return self.type_msg
