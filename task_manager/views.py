from django.shortcuts import render
from django.utils.translation import gettext


def index(request):
    message = gettext('Привет')
    return render(
        request,
        'base.html',
        context={
            'message': message
        }
    )