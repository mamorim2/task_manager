from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from tasks.models import Task


class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass"
        )
        self.client.force_authenticate(user=self.user)  # Auto-login

        self.task = Task.objects.create(
            title="API Task",
            description="Test Task",
            status="pending",
            assigned_to=self.user,
        )
        self.task_url = f"/api/tasks/{self.task.id}/"

    def test_create_task(self):
        """Test creating a task"""
        response = self.client.post(
            "/api/tasks/",
            {
                "title": "New Task",
                "description": "Created via API",
                "status": "in_progress",
                "assigned_to": self.user.id,  # Ensure this is an integer
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Task")
        self.assertEqual(
            response.data["assigned_to"], self.user.username
        )  # Ensure correct user is assigned

    def test_list_tasks(self):
        """Test retrieving tasks"""
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data["results"]), 1)

    def test_update_task(self):
        """Test updating a task"""
        response = self.client.put(
            self.task_url,
            {
                "title": "Updated Task",
                "description": "Updated",
                "status": "completed",
                "assigned_to": self.user.id,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Task")

    def test_delete_task(self):
        """Test deleting a task"""
        response = self.client.delete(self.task_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
