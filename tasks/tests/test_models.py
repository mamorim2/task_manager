from django.test import TestCase
from django.contrib.auth import get_user_model
from tasks.models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(
            title="Sample Task",
            description="Test Description",
            due_date="2025-01-01",
            status="pending",
            assigned_to=self.user
        )

    def test_task_creation(self):
        """Test task instance is created correctly"""
        self.assertEqual(self.task.title, "Sample Task")
        self.assertEqual(self.task.status, "pending")
        self.assertEqual(self.task.assigned_to, self.user)

    def test_task_str(self):
        """Test string representation"""
        self.assertEqual(str(self.task), "Sample Task")