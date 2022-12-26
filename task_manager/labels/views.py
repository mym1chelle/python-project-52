from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,\
    ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from task_manager.labels.models import Labels
from task_manager.labels.forms import CreateLabelForm
from task_manager.my_mixins import CheckConnectMixin
from constants.labels_constants import LABELS_LIST_TITLE,\
    CREATE_LABEL_SUCCESS_MESSAGE, CREATE_LABEL_BUTTON,\
    CREATE_LABEL_TITLE, CHANGE_LABEL_TITLE,\
    CHANGE_LABEL_BUTTON, CHANGE_LABEL_SUCCESS_MESSAGE,\
    DELETE_LABEL_BUTTON, DELETE_LABEL_TITLE


class AllLabelsView(LoginRequiredMixin,
                    ListView):
    model = Labels
    template_name = 'labels/labels.html'
    context_object_name = 'labels'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = LABELS_LIST_TITLE
        return context


class CreateLabelView(LoginRequiredMixin,
                      SuccessMessageMixin,
                      CreateView):
    model = Labels
    form_class = CreateLabelForm
    success_message = CREATE_LABEL_SUCCESS_MESSAGE
    success_url = reverse_lazy('labels:labels')
    template_name = 'create_edit_forms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = CREATE_LABEL_TITLE
        context['text_button'] = CREATE_LABEL_BUTTON
        return context


class UpdateLabelView(LoginRequiredMixin,
                      SuccessMessageMixin,
                      UpdateView):
    model = Labels
    form_class = CreateLabelForm
    success_message = CHANGE_LABEL_SUCCESS_MESSAGE
    success_url = reverse_lazy('labels:labels')
    template_name = 'create_edit_forms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = CHANGE_LABEL_TITLE
        context['text_button'] = CHANGE_LABEL_BUTTON
        return context


class DeleteLabelView(LoginRequiredMixin,
                      CheckConnectMixin,
                      DeleteView):
    model = Labels
    success_url = reverse_lazy('labels:labels')
    template_name = 'delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = DELETE_LABEL_TITLE
        context['text_button'] = DELETE_LABEL_BUTTON
        return context
