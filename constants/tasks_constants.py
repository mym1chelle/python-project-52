from django.utils.translation import gettext_lazy


# model
TASKS_MODEL_VERBOSE_NAME = gettext_lazy('Status')
TASKS_MODEL_VERBOSE_NAME_PLURAL = gettext_lazy('Statuses')
TASK_NAME_VN = gettext_lazy('Name')
TASK_DESCRIPTION_VN = gettext_lazy('Description')
TASK_STATUS_VN = gettext_lazy('Status')
TASK_EXECUTOR_VN = gettext_lazy('Executive')
TASK_LABEL_VN = gettext_lazy('Labels')
TASK_CREATED_BY_VN = gettext_lazy('Created_by')
TASK_CREATED_AT_VN = gettext_lazy('Created at')
TASK_UPDATED_AT_VN = gettext_lazy('Updated at')


# title
TASKS_LIST_TITLE = gettext_lazy('Tasks')
TASK_VIEW_TITLE = gettext_lazy('Task view')
CREATE_TASK_TITLE = gettext_lazy('Create a task')
CHANGE_TASK_TITLE = gettext_lazy('Change a task')
DELETE_TASK_TITLE = gettext_lazy('Change a task')

# button
CREATE_TASK_BUTTON = gettext_lazy('Create')
CHANGE_TASK_BUTTON = gettext_lazy('Change')
DELETE_TASK_BUTTON = gettext_lazy('Yes, delete')
SHOW_TASK_BUTTON = gettext_lazy('Show')

# flash-message
CREATE_TASK_SUCCESS_MESSAGE = gettext_lazy('Task successfully created')
CHANGE_TASK_SUCCESS_MESSAGE = gettext_lazy('Task successfully changed')
DELETE_TASK_SUCCESS_MESSAGE = gettext_lazy('Task successfully deleted')
DELETE_TASK_ERROR_MESSAGE = gettext_lazy('The task can only be deleted \
by its creator')
