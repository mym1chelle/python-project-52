from django import forms
from task_manager.tasks.models import Tasks


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = [
            'name',
            'description',
            'status',
            'executor',
            'labels'
        ]
