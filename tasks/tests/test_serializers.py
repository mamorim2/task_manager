from django.test import TestCase
from django.contrib.auth import get_user_model
from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskSerializerTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.task_data = {
            "title": "Test Task",
            "description": "Test Description",
            "status": "pending",
            "assigned_to": self.user.id
        }

    def test_valid_serializer(self):
        """Test valid serializer data"""
        serializer = TaskSerializer(data=self.task_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer(self):
        """Test invalid serializer (missing required field)"""
        invalid_data = self.task_data.copy()
        invalid_data.pop("title")
        serializer = TaskSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)