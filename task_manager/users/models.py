from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Users(AbstractUser):

    def __str__(self):
        return self.get_full_name