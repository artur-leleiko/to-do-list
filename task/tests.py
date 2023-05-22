from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from task.forms import TaskForm
from task.models import Task, Tag


class AllTests(TestCase):
    def setUp(self):
        Tag.objects.create(name="Test")
        Task.objects.create(
            content="Test content",
            deadline_date=datetime(2024, 12, 12, 0, 0),
        )

    def test_task_str(self):
        task = Task.objects.get(id=1)
        self.assertEqual(
            str(task),
            f"{task.content}"
        )

    def test_tag_str(self):
        tag = Tag.objects.get(id=1)
        self.assertEqual(str(tag), f"{tag.name}")

    def test_valid_form(self):
        tags = Tag.objects.all()
        data = {
            'content': 'Test content',
            'deadline': datetime(2024, 12, 12, 0, 0),
            "tags": tags,
        }
        form = TaskForm(data=data)
        self.assertTrue(form.is_valid())

    def test_correct_task_list_response_with_correct_template(self):
        response = self.client.get(reverse("task:task-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task/task_list.html")

    def test_correct_tag_list_response_with_correct_template(self):
        response = self.client.get(reverse("task:tag-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task/tag_list.html")
