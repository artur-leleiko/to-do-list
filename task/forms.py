from django import forms

from task.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        blank=True
    )
    deadline_date = forms.DateTimeField(
        widget=forms.DateTimeInput,
        required=False
    )

    class Meta:
        model = Task
        fields = ["content", "deadline_date", "tags"]
