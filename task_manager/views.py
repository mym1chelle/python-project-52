from django.views import View
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from constants.users_constants import LOGOUT_SUCCESS_MESSAGE,\
    LOGIN_TEXT_BUTTON, LOGIN_TITLE, LOGIN_SUCCESS_MESSAGE


class StartPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'startpage.html')


class LoginFormView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = LOGIN_SUCCESS_MESSAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text_button'] = LOGIN_TEXT_BUTTON
        context['title'] = LOGIN_TITLE
        return context


class LogoutFormView(SuccessMessageMixin, LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.add_message(request, messages.INFO, LOGOUT_SUCCESS_MESSAGE)
        return super().dispatch(request, *args, **kwargs)
