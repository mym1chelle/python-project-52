import django_filters
from django_filters.filters import ChoiceFilter, BooleanFilter
from django.forms import CheckboxInput
from django.db.models import Value
from django.db.models.functions import Concat
from task_manager.users.models import Users
from task_manager.labels.models import Labels
from task_manager.statuses.models import Statuses
from task_manager.tasks.models import Tasks
from constants.labels_constants import FILTER_LABEL,\
    FILTER_OWN_TASKS, FILTER_EXECUTOR, FILTER_STATUS


class FilterForTasks(django_filters.FilterSet):
    class Meta:
        model = Tasks
        fields = ['status', 'executor', 'labels']

    statuses = Statuses.objects.values_list('id', 'name').all()
    status = ChoiceFilter(
        label=FILTER_STATUS,
        choices=statuses,
    )
    all_executors = Users.objects.values_list(
        'id',
        Concat('first_name', Value(' '), 'last_name')
    ).exclude(first_name='', last_name='')
    executor = ChoiceFilter(
        label=FILTER_EXECUTOR,
        choices=all_executors,
    )
    all_labels = Labels.objects.values_list('id', 'name').all()
    labels = ChoiceFilter(
        label=FILTER_LABEL,
        choices=all_labels,
    )
    own_task = BooleanFilter(
        label=FILTER_OWN_TASKS,
        widget=CheckboxInput(),
        method='filter_own_tasks',
        field_name='own_tasks',
    )

    def filter_own_tasks(self, queryset, name, value):
        if value:
            queryset = queryset.filter(created_by=self.request.user)
        return queryset
