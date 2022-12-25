from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,\
    ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from task_manager.tasks.models import Tasks
from task_manager.tasks.forms import CreateTaskForm
from task_manager.my_mixins import CheckConnectMixin
from constants.tasks_constants import\
    TASKS_LIST_TITLE


class AllTasksView(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = TASKS_LIST_TITLE
        return context
