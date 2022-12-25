from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView,\
    ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from task_manager.tasks.models import Tasks
from task_manager.users.models import Users
from task_manager.tasks.forms import CreateTaskForm
from constants.tasks_constants import\
    TASKS_LIST_TITLE, CREATE_TASK_SUCCESS_MESSAGE,\
    CREATE_TASK_TITLE, CREATE_TASK_BUTTON,\
    TASK_VIEW_TITLE, CHANGE_TASK_TITLE,\
    CHANGE_TASK_BUTTON, CHANGE_TASK_SUCCESS_MESSAGE,\
    DELETE_TASK_TITLE, DELETE_TASK_BUTTON,\
    DELETE_TASK_ERROR_MESSAGE


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


class UpdateTaskView(LoginRequiredMixin,
                     SuccessMessageMixin,
                     UpdateView):
    model = Tasks
    form_class = CreateTaskForm
    success_message = CHANGE_TASK_SUCCESS_MESSAGE
    success_url = reverse_lazy('tasks:tasks')
    template_name = 'create_edit_forms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = CHANGE_TASK_TITLE
        context['text_button'] = CHANGE_TASK_BUTTON
        return context


class DeleteTaskView(LoginRequiredMixin,
                     SuccessMessageMixin,
                     DeleteView):
    model = Tasks
    success_url = reverse_lazy('tasks:tasks')
    template_name = 'delete.html'

    def form_valid(self, form):
        if self.object.created_by != self.request.user:
            messages.error(self.request, DELETE_TASK_ERROR_MESSAGE)
        else:
            super().form_valid(form)
        return redirect(self.success_url)


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = DELETE_TASK_TITLE
        context['text_button'] = DELETE_TASK_BUTTON
        return context
