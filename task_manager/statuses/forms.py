from django import forms
from task_manager.statuses.models import Statuses


class CreateStatusForm(forms.ModelForm):
    class Meta:
        model = Statuses
        fields = ['name']
