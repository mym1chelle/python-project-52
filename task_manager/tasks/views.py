from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,\
    ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from task_manager.tasks.models import Tasks
from task_manager.users.models import Users
from task_manager.tasks.forms import CreateTaskForm
from task_manager.my_mixins import CheckConnectMixin
from constants.tasks_constants import\
    TASKS_LIST_TITLE, CREATE_TASK_SUCCESS_MESSAGE,\
    CREATE_TASK_TITLE, CREATE_TASK_BUTTON,\
    TASK_VIEW_TITLE


class AllTasksView(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = TASKS_LIST_TITLE
        return context


class DetailTaskView(LoginRequiredMixin, DetailView):
    model = Tasks
    template_name = 'tasks/show_task.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = TASK_VIEW_TITLE
        return context



class CreateTaskView(LoginRequiredMixin,
                     SuccessMessageMixin,
                     CreateView):
    model = Tasks
    form_class = CreateTaskForm
    template_name = 'create_edit_forms.html'
    success_message = CREATE_TASK_SUCCESS_MESSAGE
    success_url = reverse_lazy('tasks:tasks')

    def form_valid(self, form):
        form.instance.created_by = Users.objects.get(pk=self.request.user.id)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = CREATE_TASK_TITLE
        context['text_button'] = CREATE_TASK_BUTTON
        return context
