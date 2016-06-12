#-*- encoding=UTF-8 -*-

from django.utils.translation import ugettext as _

class TextMessage():
	
	#User
	USER_NOT_PERMISSION = _(u"User does no have permission.")
	USER_NOT_FOUND = _(u"User no found.")
	USER_PASSWORD_ERRRO = _(u"Incorrect password.")
	USER_IS_AUTHENTICATED = _(u"User is authenticated.")
	USER_NOT_AUTHENTICATED = _(u"User is no authenticated.")
	USER_CREATED_SUCCESS = _(u"User created successfully.")
	USER_CREATED_ERROR = _(u"Failed to create user.")
	USER_ADD_GROUP_ERROR = _(u"Failed to add group.")
	USER_GROUP_NOT_FOUND = _(u"User group no found.")
	
	EMAIL_RECOVER_PASSWORD_SUCCESS = _(u"Email of recover password send success.")
	EMAIL_RECOVER_PASSWORD_ERROR = _(u"Email of recover password send error.")
	
	
	CHANGED_PASSWORD_SUCCESS = _(u"Password changed success.")
	USERNAME_OR_PASSWORD_INCORRECT = _(u"Username or password incorrect.")
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

	#Classe
	CLASSE_SUCCESS_ADD = _(u"Classe successfully added.")
	CLASSE_ERROR_ADD = _(u"Error adding classe.")
 	
	CLASSE_SUCCESS_EDIT = _(u"Classe successfully edit.")
	CLASSE_ERROR_EDIT = _(u"Error edit classe.")
 	
	CLASSE_SUCCESS_REM = _(u"Classe successfully removed.")
	CLASSE_ERROR_REM = _(u"Error remove classe.")
	
	CLASSE_SUCCESS_RESTORE = _(u"Classe successfully restored.")
	CLASSE_ERROR_RESTORE = _(u"Error restore classe.")
 
	CLASSE_SUCCESS_JOIND = _(u"Enrollment in the class was successful.")
	CLASSE_ERROR_JOIND = _(u"Error during their enrollment in the class.")

	CLASSE_SUCCESS_OUT = _(u"Out of successfully class.")
	CLASSE_ERROR_OUT = _(u"Error out of the class.")

	CLASSE_SUCCESS_SET = _(u"Class assigned as the default.")
	CLASSE_ERROR_SET = _(u"Error when assigning class as standard.")

	CLASSE_NOT_FOUND = _(u"Classe no found.")




	#Discipline
	DISCIPLINE_SUCCESS_ADD = _(u"Discipline successfully added.")
	DISCIPLINE_ERROR_ADD = _(u"Error adding discipline.")
 	
	DISCIPLINE_SUCCESS_EDIT = _(u"Discipline successfully edit.")
	DISCIPLINE_ERROR_EDIT = _(u"Error edit discipline.")
 	
	DISCIPLINE_SUCCESS_REM = _(u"Discipline successfully removed.")
	DISCIPLINE_ERROR_REM = _(u"Error remove discipline.")
	
	DISCIPLINE_SUCCESS_RESTORE = _(u"Discipline successfully restored.")
	DISCIPLINE_ERROR_RESTORE = _(u"Error restore discipline.")
 
	DISCIPLINE_NOT_FOUND = _(u"Discipline no found.")

	#Lesson
 	LESSON_SUCCESS_ADD = _(u"Lesson successfully added.")
 	LESSON_ERROR_ADD = _(u"Error adding lesson.")
 	
 	LESSON_SUCCESS_EDIT = _(u"Lesson successfully edit.")
 	LESSON_ERROR_EDIT = _(u"Error edit lesson.")
 	
 	LESSON_SUCCESS_REM = _(u"Lesson successfully removed.")
 	LESSON_ERROR_REM = _(u"Error remove lesson.")
 	
 	LESSON_SUCCESS_RESTORE = _(u"Lesson successfully restored.")
	LESSON_ERROR_RESTORE = _(u"Error restore lesson.")
 
 	LESSON_NOT_FOUND = _(u"Lesson no found.")
 	LESSON_SUCCESS_COMPLETED = _(u"Lesson successfully completed.")
 	
 	LESSON_SUCCESS_RESET = _(u"Lesson successfully reset.")
 	
 	LESSON_NOT_REMAINING_JUMPS = _(u"Lesson no remaining jumps.")
 	
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
 
 	QUESTION_NOT_FOUND = _(u"Question no found.")
 	
 	QUESTION_SUCCESS_REPLY = _(u"Your reply is correct.")
 	QUESTION_ERROR_REPLY = _(u"Your reply is incorrect.")
 	QUESTION_REPLY = _(u"Question is reply.")
 	
 	QUESTION_SUCCESS_JUMP = _(u"Jump realization with successfully.")
 	QUESTION_JUMP = _(u"Question is jump.")
 	QUESTION_ERROR_JUMP = _(u"Question error in jump.")
 	QUESTION_IMPOSSIBLE_JUMP = _(u"Impossible to make the leap.")
 	
 	QUESTION_NOT_FOUND_IN_LESSON = _(u"Question no found in lesson.")
 	
 	#Item
 	ITEM_NOT_FOUND = _(u"Item no found.")
 	ITEM_NOT_FOUND_IN_QUESTION = _(u"Item no found in question.")
 	
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
 
 	VIDEO_NOT_FOUND = _(u"Video no found.")
 	VIDEO_NOT_FOUND_IN_LESSON = _(u"Video no found in lesson.")
 	
 	
 	#Category
 	CATEGORY_SUCCESS_ADD = _(u"Category successfully added.")
 	CATEGORY_ERROR_ADD = _(u"Error adding category.")
 	
 	CATEGORY_SUCCESS_EDIT = _(u"Category successfully edit.")
 	CATEGORY_ERROR_EDIT = _(u"Error edit category.")
 
 	CATEGORY_SUCCESS_REM = _(u"Category successfully removed.")
 	CATEGORY_ERROR_REM = _(u"Error remove category.")
 	
 	CATEGORY_SUCCESS_RESTORE = _(u"Category successfully restored.")
	CATEGORY_ERROR_RESTORE = _(u"Error restore category.")
 
 	CATEGORY_NOT_FOUND = _(u"Category no found.")
 	
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
 
 	TOPIC_NOT_FOUND = _(u"Topic no found.")
 	
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
 
 
 	COMMENT_NOT_FOUND = _(u"Comment no found.")
 	
 	#Contact
 	MESSAGE_SUCCESS_ADD = _(u"Message successfully added.")
 	MESSAGE_ERROR_ADD = _(u"Error adding message.")
 	
 	MESSAGE_SUCCESS_EDIT = _(u"Message successfully edit.")
 	MESSAGE_ERROR_EDIT = _(u"Error edit message.")
 	
 	MESSAGE_SUCCESS_REM = _(u"Message successfully removed.")
 	MESSAGE_ERROR_REM = _(u"Error remove message.")
 	
 	MESSAGE_SUCCESS_RESTORE = _(u"Message successfully restored.")
	MESSAGE_ERROR_RESTORE = _(u"Error restore message.")
	
 
 	MESSAGE_NOT_FOUND = _(u"Message no found.")
 	
 	
 	

	
	#Person
 	USER_SUCCESS_ADD = _(u"User successfully added.")
 	USER_ERROR_ADD = _(u"Error adding user.")
 	
 	USER_SUCCESS_EDIT = _(u"User successfully edit.")
 	USER_ERROR_EDIT = _(u"Error edit user.")
 	
 	USER_SUCCESS_REM = _(u"User successfully removed.")
 	USER_ERROR_REM = _(u"Error remove user.")
 	
 	USER_SUCCESS_RESTORE = _(u"User successfully restored.")
	USER_ERROR_RESTORE = _(u"Error restore user.")
 
 	USER_NOT_FOUND = _(u"User no found.")
 	
 	#Statistics
 	
 	STATISTIC_NOT_FOUND = _(u"Statistic no found.")



	#Parameters
	ERROR_GET_PARAMETERS = _(u"Error pick up the parameters.")
	
	#Results
	NO_RESULTS_FOUND  = _(u"No results found.")
	
	#Request
	METHOD_NOT_POST  = _(u"Method no is POST.")
	METHOD_NOT_GET  = _(u"Method no is GET.")

	#Messages
	MESSAGE_SUCCESS_SEND = _(u"Message successfully send.")
	
	#KEYS
	KEY_NOT_FOUND = _(u"Key no found.")
	KEY_ERROR_REMOVE_USED = _(u"Error removing the key, user ever used.")
	
	#ACCOUNT
	ACCOUNT_SUCCESS_REMOVED = _(u"Account success removed.")

	SEARCH_ERROR_SIZE = _(u"There was an error in your search, try using no more than 27 characters in the search.")