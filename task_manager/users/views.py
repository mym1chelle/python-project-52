from django.contrib.auth.mixins import AccessMixin
from task_manager.users.forms import CreateUserForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView,\
    ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect

from task_manager.users.models import Users
from task_manager.constants import *


class ChangeUserInfoMixin(AccessMixin):
    success_url = ''
    
    def dispatch(self, request, *args, **kwargs):
        if kwargs.get('pk') != self.request.user.id:
            messages.error(self.request, CHANGE_USER_ERROR_MESSAGE)
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class CheckAuthenticatedMixin(AccessMixin):
    error_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        messages.error(self.request, NOT_AUTH_ERROR_MESSAGE)
        return redirect(self.error_url)


class AllUsersView(ListView):
    model=Users
    template_name = 'users.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = USERS_LIST_TITLE
        return data


class CreateUser(SuccessMessageMixin, CreateView):
    "Create a user."
    model = Users
    template_name = 'create_edit_forms.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    success_message = CREATE_USER_SUCCESS_MESSAGE
    
    def get_context_data(self, **kwargs):
        "Set up the title and the button."
        context = super().get_context_data(**kwargs)
        context['text_button'] = REGISTRETION_USER_TEXT_BUTTON
        context['title'] = CREATE_USER_TITLE
        return context


class UserUpdateView(SuccessMessageMixin,
                     CheckAuthenticatedMixin,
                     ChangeUserInfoMixin,
                     UpdateView):
    model = Users
    template_name = 'create_edit_forms.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('users')
    success_message = CHANGE_USER_SUCCESS_MESSAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text_button'] = CHANGE_USER_TEXT_BUTTON
        context['title'] = CHANGE_USER_TITLE
        return context


class UserDeleteView(SuccessMessageMixin,
                     CheckAuthenticatedMixin,
                     ChangeUserInfoMixin,
                     DeleteView):
    model = Users
    template_name = 'delete.html'
    success_message = DELETE_USER_SUCCESS_MESSAGE
    success_url = reverse_lazy('users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = DELETE_USER_TITLE
        context['text_button'] = DELETE_USER_TEXT_BUTTON
        return context
