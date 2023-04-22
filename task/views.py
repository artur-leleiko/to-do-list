from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from task.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    context_object_name = "task_list"
    template_name = "task/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "task/task_delete.html"
    success_url = reverse_lazy("task:task-list")


class TaskUpdateStatus(View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("task:task-list")


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()
    context_object_name = "tag_list"
    template_name = "tag/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "tag/tag_form.html"
    success_url = reverse_lazy("tag:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "tag/tag_form.html"
    success_url = reverse_lazy("tag:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tag/tag_delete.html"
    success_url = reverse_lazy("tag:tag-list")
