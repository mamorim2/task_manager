from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from tasks.models import Task

class TaskPermissionTestCase(APITestCase):
    def setUp(self):
        self.owner = get_user_model().objects.create_user(username='owner', password='testpass')
        self.other_user = get_user_model().objects.create_user(username='otheruser', password='testpass')

        self.task = Task.objects.create(title="Owner Task", assigned_to=self.owner)
        self.task_url = f"/api/tasks/{self.task.id}/"

    def test_owner_can_edit(self):
        """Test that the owner can edit their task"""
        self.client.force_authenticate(user=self.owner)
        response = self.client.patch(self.task_url, {"title": "Updated by Owner"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_owner_cannot_edit(self):
        """Test that a non-owner cannot edit the task"""
        self.client.force_authenticate(user=self.other_user)
        response = self.client.patch(self.task_url, {"title": "Updated by Other"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)