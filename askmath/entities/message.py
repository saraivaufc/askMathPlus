#-*- encoding=UTF-8 -*-

from django.utils.translation import ugettext as _


class TypeMessage():
	SUCCESS = _('SUCCESS')
	INFO = _('INFO')
	WARNING = _('WARNING')
	ERROR = _('ERROR')

class TextMessage():
	
	#User
	USER_NOT_PERMISSION = _(u"User does not have permission.")
	USER_NOT_FOUND = _(u"User not found.")
	USER_PASSWORD_ERRRO = _(u"Incorrect password.")
	USER_IS_AUTHENTICATED = _(u"User is authenticated.")
	USER_NOT_AUTHENTICATED = _(u"User is not authenticated.")
	USER_CREATED_SUCCESS = _(u"User created successfully.")
	USER_CREATED_ERROR = _(u"Failed to create user.")
	USER_ADD_GROUP_ERROR = _(u"Failed to add group.")
	USER_TYPE_NOT_FOUND = _(u"User type not found.")
	
	EMAIL_RECOVER_PASSWORD_SUCCESS = _(u"Email of recover password send success.")
	EMAIL_RECOVER_PASSWORD_ERROR = _(u"Email of recover password send error.")
	
	
	CHANGED_PASSWORD_SUCCESS = _(u"Password changed success.")
	PASSWORD_INCORRECT = _(u"Password incorrect.")


	#Login and Logout
	LOGIN_SUCCESS = _(u"Login successfully performed..") 
	LOGIN_ERROR = _(u"Failed to perform login.") 
	LOGOUT_SUCCESS = _(u"Logout successfully performed.")
	LOGOUT_ERROR = _(u"Failed to perform logout.")

	#Requests
	POST_REQUIRED = _(u"POST required.")

	ERROR = _(u"Error, Contact Administrator.")

	#Forms
	ERROR_FORM = _(u"There was an error on the form.")


	#Discipline
	DISCIPLINE_SUCCESS_ADD = _(u"Discipline successfully added.")
	DISCIPLINE_ERROR_ADD = _(u"Error adding discipline.")
 	
	DISCIPLINE_SUCCESS_EDIT = _(u"Discipline successfully edit.")
	DISCIPLINE_ERROR_EDIT = _(u"Error edit discipline.")
 	
	DISCIPLINE_SUCCESS_REM = _(u"Discipline successfully removed.")
	DISCIPLINE_ERROR_REM = _(u"Error remove discipline.")
	
	DISCIPLINE_SUCCESS_RESTORE = _(u"Discipline successfully restored.")
	DISCIPLINE_ERROR_RESTORE = _(u"Error restore discipline.")
 
	DISCIPLINE_NOT_FOUND = _(u"Discipline not found.")

	#Lesson
 	LESSON_SUCCESS_ADD = _(u"Lesson successfully added.")
 	LESSON_ERROR_ADD = _(u"Error adding lesson.")
 	
 	LESSON_SUCCESS_EDIT = _(u"Lesson successfully edit.")
 	LESSON_ERROR_EDIT = _(u"Error edit lesson.")
 	
 	LESSON_SUCCESS_REM = _(u"Lesson successfully removed.")
 	LESSON_ERROR_REM = _(u"Error remove lesson.")
 	
 	LESSON_SUCCESS_RESTORE = _(u"Lesson successfully restored.")
	LESSON_ERROR_RESTORE = _(u"Error restore lesson.")
 
 	LESSON_NOT_FOUND = _(u"Lesson not found.")
 	LESSON_SUCCESS_COMPLETED = _(u"Lesson successfully completed.")
 	
 	LESSON_SUCCESS_RESET = _(u"Lesson successfully reset.")
 	
 	LESSON_NOT_REMAINING_JUMPS = _(u"Lesson not remaining jumps.")
 	
 	#Question
 	QUESTION_SUCCESS_ADD = _(u"Question successfully added.")
 	QUESTION_ERROR_ADD = _(u"Error adding question.")
 	
 	QUESTION_SUCCESS_EDIT = _(u"Question successfully edit.")
 	QUESTION_ERROR_EDIT = _(u"Error edit question.")
 	
 	QUESTION_SUCCESS_REM = _(u"Question successfully removed.")
 	QUESTION_ERROR_REM = _(u"Error remove question.")
 	
 	QUESTION_SUCCESS_RESTORE = _(u"Question successfully restored.")
	QUESTION_ERROR_RESTORE = _(u"Error restore question.")
	
	QUESTION_SUCCESS_SORT = _(u"Question successfully sorted.")
	QUESTION_ERROR_SORT = _(u"Error sorted question.")
 
 	QUESTION_NOT_FOUND = _(u"Question not found.")
 	
 	QUESTION_SUCCESS_REPLY = _(u"Your reply is correct.")
 	QUESTION_ERROR_REPLY = _(u"Your reply is incorrect.")
 	QUESTION_REPLY = _(u"Question is reply.")
 	
 	QUESTION_SUCCESS_JUMP = _(u"Jump realization with successfully.")
 	QUESTION_JUMP = _(u"Question is jump.")
 	QUESTION_ERROR_JUMP = _(u"Question error in jump.")
 	
 	QUESTION_NOT_FOUND_IN_LESSON = _(u"Question not found in lesson.")
 	
 	#Item
 	ITEM_NOT_FOUND = _(u"Item not found.")
 	ITEM_NOT_FOUND_IN_QUESTION = _(u"Item not found in question.")
 	
	#Video
 	VIDEO_SUCCESS_ADD = _(u"Video successfully added.")
 	VIDEO_ERROR_ADD = _(u"Error adding video.")
 	
 	VIDEO_SUCCESS_EDIT = _(u"Video successfully edit.")
 	VIDEO_ERROR_EDIT = _(u"Error edit video.")
 	
 	VIDEO_SUCCESS_REM = _(u"Video successfully removed.")
 	VIDEO_ERROR_REM = _(u"Error remove video.")
 	
 	VIDEO_SUCCESS_RESTORE = _(u"Video successfully restored.")
	VIDEO_ERROR_RESTORE = _(u"Error restore video.")
	
	VIDEO_SUCCESS_SORT = _(u"Video successfully sorted.")
	VIDEO_ERROR_SORT = _(u"Error sorted video.")
 
 	VIDEO_NOT_FOUND = _(u"Video not found.")
 	VIDEO_NOT_FOUND_IN_LESSON = _(u"Video not found in lesson.")
 	
 	
 	#Category
 	CATEGORY_SUCCESS_ADD = _(u"Category successfully added.")
 	CATEGORY_ERROR_ADD = _(u"Error adding category.")
 	
 	CATEGORY_SUCCESS_EDIT = _(u"Category successfully edit.")
 	CATEGORY_ERROR_EDIT = _(u"Error edit category.")
 
 	CATEGORY_SUCCESS_REM = _(u"Category successfully removed.")
 	CATEGORY_ERROR_REM = _(u"Error remove category.")
 	
 	CATEGORY_SUCCESS_RESTORE = _(u"Category successfully restored.")
	CATEGORY_ERROR_RESTORE = _(u"Error restore category.")
 
 	CATEGORY_NOT_FOUND = _(u"Category not found.")
 	
 	#Topic
 	TOPIC_SUCCESS_ADD = _(u"Topic successfully added.")
 	TOPIC_ERROR_ADD = _(u"Error adding topic.")
 	
 	TOPIC_SUCCESS_EDIT = _(u"Topic successfully edit.")
 	TOPIC_ERROR_EDIT = _(u"Error edit topic.")
 
 	TOPIC_SUCCESS_REM = _(u"Topic successfully removed.")
 	TOPIC_ERROR_REM = _(u"Error remove topic.")
 	
 	TOPIC_SUCCESS_RESTORE = _(u"Topic successfully restored.")
	TOPIC_ERROR_RESTORE = _(u"Error restore topic.")
	
	TOPIC_SUCCESS_LIKE = _(u"Topic successfully liked.")
	TOPIC_ERROR_LIKE = _(u"Error like topic.")
	TOPIC_SUCCESS_UNLIKE = _(u"Topic successfully unliked.")
	TOPIC_ERROR_UNLIKE = _(u"Error unlike topic.")
 
 	TOPIC_NOT_FOUND = _(u"Topic not found.")
 	
 	#Comment
 	COMMENT_SUCCESS_ADD = _(u"Comment successfully added.")
 	COMMENT_ERROR_ADD = _(u"Error adding comment.")
 	
 	COMMENT_SUCCESS_EDIT = _(u"Comment successfully edit.")
 	COMMENT_ERROR_EDIT = _(u"Error edit comment.")
 
 	COMMENT_SUCCESS_REM = _(u"Comment successfully removed.")
 	COMMENT_ERROR_REM = _(u"Error remove comment.")
 	
 	COMMENT_SUCCESS_RESTORE = _(u"Comment successfully restored.")
	COMMENT_ERROR_RESTORE = _(u"Error restore comment.")

	COMMENT_SUCCESS_LIKE = _(u"Comment successfully liked.")
	COMMENT_ERROR_LIKE = _(u"Error like comment.")
 
 
 	COMMENT_NOT_FOUND = _(u"Comment not found.")
 	
 	#Contact
 	CONTACT_SUCCESS_ADD = _(u"Contact successfully added.")
 	CONTACT_ERROR_ADD = _(u"Error adding contact.")
 	
 	CONTACT_SUCCESS_EDIT = _(u"Contact successfully edit.")
 	CONTACT_ERROR_EDIT = _(u"Error edit contact.")
 	
 	CONTACT_SUCCESS_REM = _(u"Contact successfully removed.")
 	CONTACT_ERROR_REM = _(u"Error remove contact.")
 	
 	CONTACT_SUCCESS_RESTORE = _(u"Contact successfully restored.")
	CONTACT_ERROR_RESTORE = _(u"Error restore contact.")
	
 
 	CONTACT_NOT_FOUND = _(u"Contact not found.")
 	
 	
 	

	
	#Person
 	PERSON_SUCCESS_ADD = _(u"Person successfully added.")
 	PERSON_ERROR_ADD = _(u"Error adding person.")
 	
 	PERSON_SUCCESS_EDIT = _(u"Person successfully edit.")
 	PERSON_ERROR_EDIT = _(u"Error edit person.")
 	
 	PERSON_SUCCESS_REM = _(u"Person successfully removed.")
 	PERSON_ERROR_REM = _(u"Error remove person.")
 	
 	PERSON_SUCCESS_RESTORE = _(u"Person successfully restored.")
	PERSON_ERROR_RESTORE = _(u"Error restore person.")
 
 	PERSON_NOT_FOUND = _(u"Person not found.")
 	
 	#Statistics
 	
 	STATISTIC_NOT_FOUND = _(u"Statistic not found.")



	#Parameters
	ERROR_GET_PARAMETERS = _(u"Error pick up the parameters.")
	
	#Results
	NO_RESULTS_FOUND  = _(u"No results found.")
	
	#Request
	METHOD_NOT_POST  = _(u"Method not is POST.")
	METHOD_NOT_GET  = _(u"Method not is GET.")

	#Messages
	MESSAGE_SUCCESS_SEND = _(u"Message successfully send.")
	
	#KEYS
	KEY_NOT_FOUND = _(u"Key not found.")
	KEY_ERROR_REMOVE_USED = _(u"Error removing the key, user ever used.")
	
	#ACCOUNT
	ACCOUNT_SUCCESS_REMOVED = _(u"Account success removed.")

	SEARCH_ERROR_SIZE = _(u"Ocorreu um erro na sua busca, tente utilizar no máximo 27 caracteres na busca.")
	
	



class Message():
	text = ''
	type_msg =None 
	def __init__(self, text, type_msg):
		self.text = unicode(text)
		self.type_msg = type_msg

	def type(self):
		return self.type_msg
