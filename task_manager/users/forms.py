from task_manager.users.models import Users
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = Users
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        ]
