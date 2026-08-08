from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class HealthCheckTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_health_check_returns_200(self):
        response = self.client.get("/api/v1/health/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_health_check_returns_expected_payload(self):
        response = self.client.get("/api/v1/health/")

        self.assertEqual(
            response.json(),
            {
                "status": "ok",
                "service": "django-api",
            },
        )