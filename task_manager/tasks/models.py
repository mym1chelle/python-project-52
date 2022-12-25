from django.db import models
from task_manager.users.models import Users
from task_manager.statuses.models import Statuses
from constants.tasks_constants import\
    TASK_NAME_VN, TASK_DESCRIPTION_VN,\
    TASK_STATUS_VN, TASK_CREATED_BY_VN,\
    TASK_EXECUTOR_VN, TASK_CREATED_AT_VN,\
    TASK_UPDATED_AT_VN, TASKS_MODEL_VERBOSE_NAME,\
    TASKS_MODEL_VERBOSE_NAME_PLURAL


class Tasks(models.Model):

    class Meta:
        verbose_name = TASKS_MODEL_VERBOSE_NAME
        verbose_name_plural = TASKS_MODEL_VERBOSE_NAME_PLURAL
        ordering = ['id']

    name = models.CharField(
        max_length=100,
        null=False,
        verbose_name=TASK_NAME_VN
    )
    description = models.TextField(
        blank=True,
        verbose_name=TASK_DESCRIPTION_VN
    )
    status = models.ForeignKey(
        Statuses,
        on_delete=models.PROTECT,
        null=True,
        verbose_name=TASK_STATUS_VN,
        related_name='task_status'
    )
    created_by = models.ForeignKey(
        Users,
        on_delete=models.PROTECT,
        null=False,
        verbose_name=TASK_CREATED_BY_VN,
        related_name='task_created_by'
    )
    executor = models.ForeignKey(
        Users,
        on_delete=models.PROTECT,
        null=True,
        verbose_name=TASK_EXECUTOR_VN,
        related_name='task_executor',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=TASK_CREATED_AT_VN
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=TASK_UPDATED_AT_VN
    )

    def __str__(self):
        return self.name
