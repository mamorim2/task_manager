from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass"
        )

    def test_obtain_jwt_token(self):
        """Test obtaining a JWT token"""
        response = self.client.post(
            "/api/auth/token/", {"username": "testuser", "password": "testpass"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_invalid_login(self):
        """Test invalid login attempt"""
        response = self.client.post(
            "/api/auth/token/", {"username": "wronguser", "password": "wrongpass"}
        )
        print(f"Response data: {response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", response.data)
