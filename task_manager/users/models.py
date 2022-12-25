from django.contrib.auth.models import AbstractUser
from constants.users_constants import\
    USERS_MODEL_VERBOSE_NAME_PLURAL,\
    USERS_MODEL_VERBOSE_NAME


class Users(AbstractUser):
    class Meta:
        verbose_name = USERS_MODEL_VERBOSE_NAME
        verbose_name_plural = USERS_MODEL_VERBOSE_NAME_PLURAL

    def __str__(self):
        return self.get_full_name
