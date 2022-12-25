from django.utils.translation import gettext_lazy


# model
STATUSES_MODEL_VERBOSE_NAME = gettext_lazy('Status')
STATUSES_MODEL_VERBOSE_NAME_PLURAL = gettext_lazy('Statuses')
STATUS_VERBOSE_NAME = gettext_lazy('Name')
CREATED_AT_VERBOSE_NAME = gettext_lazy('Created at')
UPDATED_AT_VERBOSE_NAME = gettext_lazy('Updated at')

# title
STATUSES_LIST_TITLE = gettext_lazy('Statuses')
CREATE_STATUS_TITLE = gettext_lazy('Create a status')
CHANGE_STATUS_TITLE = gettext_lazy('Change a status')
DELETE_STATUS_TITLE = gettext_lazy('Delete a status')

# button
CREATE_STATUS_BUTTON = gettext_lazy('Create')
CHANGE_STATUS_BUTTON = gettext_lazy('Change')
DELETE_STATUS_BUTTON = gettext_lazy('Yes, delete')

# flash-message
CREATE_STATUS_SUCCESS_MESSAGE = gettext_lazy('Status successfully created')
CHANGE_STATUS_SUCCESS_MESSAGE = gettext_lazy('Status successfully changed')
DELETE_STATUS_SUCCESS_MESSAGE = gettext_lazy('Status successfully deleted')
DELETE_STATUS_ERROR_MESSAGE = gettext_lazy('Cannot delete a status in use')
