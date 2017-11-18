# Django imports
from django import forms

# Tasks app imports
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'priority',
            'user_who_submitted',
            'files',
        )
