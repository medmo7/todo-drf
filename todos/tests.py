from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="todo",
            body="todo body"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "todo")
        self.assertEqual(self.todo.body, "todo body")
        self.assertEqual(str(self.todo), "todo")
    
    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.all().count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        response = self.client.get(reverse("todo_detail", args=[self.todo.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.all().count(), 1)
        self.assertContains(response, "todo")
