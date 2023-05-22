from django import forms

from task.models import Tag, Task


class TaskForm(forms.ModelForm):
    content = forms.CharField(label="Task")
    deadline_date = forms.DateTimeField(
        widget=forms.DateTimeInput,
        required=False,
        help_text="(e.g. 2025-01-01 16:30)"
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        blank=True
    )

    class Meta:
        model = Task
        fields = ["content", "deadline_date", "tags"]
