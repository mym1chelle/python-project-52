from django.utils.translation import gettext_lazy


# model
LABELS_MODEL_VERBOSE_NAME = gettext_lazy('Label')
LABELS_MODEL_VERBOSE_NAME_PLURAL = gettext_lazy('Labels')
LABEL_NAME_VN = gettext_lazy('Name')
LABEL_CREATED_AT_VN = gettext_lazy('Created at')
LABEL_UPDATED_AT_VN = gettext_lazy('Updated at')


# title
LABELS_LIST_TITLE = gettext_lazy('Labels')
CREATE_LABEL_TITLE = gettext_lazy('Create a label')
CHANGE_LABEL_TITLE = gettext_lazy('Change a label')
DELETE_LABEL_TITLE = gettext_lazy('Delete a label')

# button
CREATE_LABEL_BUTTON = gettext_lazy('Create')
CHANGE_LABEL_BUTTON = gettext_lazy('Change')
DELETE_LABEL_BUTTON = gettext_lazy('Yes, delete')

# flash-message
CREATE_LABEL_SUCCESS_MESSAGE = gettext_lazy('Label successfully created')
CHANGE_LABEL_SUCCESS_MESSAGE = gettext_lazy('Label successfully changed')
DELETE_LABEL_SUCCESS_MESSAGE = gettext_lazy('Label successfully deleted')
DELETE_LABEL_ERROR_MESSAGE = gettext_lazy('Cannot delete a label in use')