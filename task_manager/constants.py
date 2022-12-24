from django.utils.translation import gettext_lazy


# button
LOGIN_TEXT_BUTTON = gettext_lazy('Login')
REGISTRETION_USER_TEXT_BUTTON = gettext_lazy('Register')
CHANGE_USER_TEXT_BUTTON = gettext_lazy('Change')
DELETE_USER_TEXT_BUTTON = gettext_lazy('Yes, delete')

# flash message
LOGIN_SUCCESS_MESSAGE = gettext_lazy('Logged in successfully')
LOGOUT_SUCCESS_MESSAGE = gettext_lazy('Logged out successfully')
CHANGE_USER_ERROR_MESSAGE = gettext_lazy('You do not have a permission to change another user')
NOT_AUTH_ERROR_MESSAGE = gettext_lazy('You are not authorized. Please, log in.')
CREATE_USER_SUCCESS_MESSAGE = gettext_lazy('User successfully created')
CHANGE_USER_SUCCESS_MESSAGE = gettext_lazy('User successfully changed')
DELETE_USER_SUCCESS_MESSAGE = gettext_lazy('User was successfuly delete')

# title
CREATE_USER_TITLE = gettext_lazy('Create a user')
LOGIN_TITLE = gettext_lazy('Login in')
CHANGE_USER_TITLE = gettext_lazy('Change a user')
DELETE_USER_TITLE = gettext_lazy('Delete a user')
USERS_LIST_TITLE = gettext_lazy('Users')
