from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from constants.users_constants import\
    DELETE_USER_SUCCESS_MESSAGE, DELETE_USER_ERROR_MESSAGE
from constants.statuses_constants import\
    DELETE_STATUS_SUCCESS_MESSAGE, DELETE_STATUS_ERROR_MESSAGE


SUCCESS_MESSAGES = {
    'Users': DELETE_USER_SUCCESS_MESSAGE,
    'Statuses': DELETE_STATUS_SUCCESS_MESSAGE,
}
ERROR_MESSAGES = {
    'Users': DELETE_USER_ERROR_MESSAGE,
    'Statuses': DELETE_STATUS_ERROR_MESSAGE,
}


class CheckConnectMixin(AccessMixin):
    def form_valid(self, form):
        "Check if any other objects are linked to the given object."
        try:
            model_name = str(self.object.__class__.__name__)
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, ERROR_MESSAGES[model_name])
        else:
            messages.success(self.request, SUCCESS_MESSAGES[model_name])
        return redirect(self.get_success_url())
