from django.db import models
from constants.labels_constants import\
    LABEL_NAME_VN, LABEL_CREATED_AT_VN,\
    LABEL_UPDATED_AT_VN,LABELS_MODEL_VERBOSE_NAME,\
    LABELS_MODEL_VERBOSE_NAME_PLURAL


class Labels(models.Model):

    class Meta:
        verbose_name = LABELS_MODEL_VERBOSE_NAME
        verbose_name_plural = LABELS_MODEL_VERBOSE_NAME_PLURAL
        ordering = ['id']

    name = models.CharField(max_length=100, verbose_name=LABEL_NAME_VN)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=LABEL_CREATED_AT_VN
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=LABEL_UPDATED_AT_VN
    )

    def __str__(self):
        return self.name
