from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,\
    ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from task_manager.statuses.models import Statuses
from constants.statuses_constants import\
    STATUSES_LIST_TITLE, CREATE_STATUS_TITLE,\
    CREATE_STATUS_BUTTON, CREATE_STATUS_SUCCESS_MESSAGE,\
    CHANGE_STATUS_BUTTON, CHANGE_STATUS_SUCCESS_MESSAGE,\
    CHANGE_STATUS_TITLE, DELETE_STATUS_BUTTON,\
    DELETE_STATUS_SUCCESS_MESSAGE, DELETE_STATUS_TITLE
from task_manager.statuses.forms import CreateStatusForm
from task_manager.my_mixins import CheckConnectMixin


class AllStatusesView(LoginRequiredMixin, ListView):
    model = Statuses
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = STATUSES_LIST_TITLE
        return context


class CreateStatusView(LoginRequiredMixin,
                       SuccessMessageMixin,
                       CreateView):
    model = Statuses
    template_name = 'create_edit_forms.html'
    success_url = reverse_lazy('statuses:statuses')
    form_class = CreateStatusForm
    success_message = CREATE_STATUS_SUCCESS_MESSAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = CREATE_STATUS_TITLE
        context['text_button'] = CREATE_STATUS_BUTTON
        return context


class UpdateStatusView(LoginRequiredMixin,
                       SuccessMessageMixin,
                       UpdateView):
    model = Statuses
    template_name = 'create_edit_forms.html'
    success_url = reverse_lazy('statuses:statuses')
    form_class = CreateStatusForm
    success_message = CHANGE_STATUS_SUCCESS_MESSAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = CHANGE_STATUS_TITLE
        context['text_button'] = CHANGE_STATUS_BUTTON
        return context


class DeleteStatusView(LoginRequiredMixin,
                       CheckConnectMixin,
                       DeleteView):
    model = Statuses
    template_name = 'delete.html'
    success_url = reverse_lazy('statuses:statuses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = DELETE_STATUS_TITLE
        context['text_button'] = DELETE_STATUS_BUTTON
        return context


