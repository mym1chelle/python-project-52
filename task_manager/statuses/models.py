from django.db import models
from constants.statuses_constants import\
    STATUSES_MODEL_VERBOSE_NAME,\
    STATUSES_MODEL_VERBOSE_NAME_PLURAL,\
    STATUS_VERBOSE_NAME,\
    CREATED_AT_VERBOSE_NAME,\
    UPDATED_AT_VERBOSE_NAME


class Statuses(models.Model):
    class Meta:
        verbose_name = STATUSES_MODEL_VERBOSE_NAME
        verbose_name_plural = STATUSES_MODEL_VERBOSE_NAME_PLURAL

    name = models.CharField(max_length=100, null=False, verbose_name=STATUS_VERBOSE_NAME)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=CREATED_AT_VERBOSE_NAME)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=UPDATED_AT_VERBOSE_NAME)

    def __str__(self):
        return self.name
