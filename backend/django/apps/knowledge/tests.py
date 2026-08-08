from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import KnowledgeResource


class KnowledgeResourceAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.resource_1 = KnowledgeResource.objects.create(
            title="Django REST Framework Guide",
            description="A guide to building APIs with DRF.",
            resource_type=KnowledgeResource.ResourceType.DOCUMENTATION,
            source_url="https://www.django-rest-framework.org/",
            author="Django REST Framework",
            is_active=True,
        )

        self.resource_2 = KnowledgeResource.objects.create(
            title="Research Paper on AI",
            description="A research paper about artificial intelligence.",
            resource_type=KnowledgeResource.ResourceType.PAPER,
            source_url="https://example.com/ai-paper",
            author="AI Researcher",
            is_active=False,
        )

    def test_list_resources(self):
        response = self.client.get("/api/v1/knowledge/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_by_resource_type(self):
        response = self.client.get(
            "/api/v1/knowledge/",
            {"resource_type": "paper"},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data[0]["resource_type"],
            "paper",
        )

    def test_filter_by_active_status(self):
        response = self.client.get(
            "/api/v1/knowledge/",
            {"is_active": "true"},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertTrue(response.data[0]["is_active"])

    def test_ordering_by_title(self):
        response = self.client.get(
            "/api/v1/knowledge/",
            {"ordering": "title"},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data[0]["title"],
            "Django REST Framework Guide",
        )

    def test_create_resource(self):
        payload = {
            "title": "FastAPI Documentation",
            "description": "Official FastAPI documentation.",
            "resource_type": "documentation",
            "source_url": "https://fastapi.tiangolo.com/",
            "author": "FastAPI",
            "is_active": True,
        }

        response = self.client.post(
            "/api/v1/knowledge/",
            payload,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            KnowledgeResource.objects.count(),
            3,
        )

    def test_retrieve_resource(self):
        response = self.client.get(
            f"/api/v1/knowledge/{self.resource_1.id}/"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["title"],
            "Django REST Framework Guide",
        )

    def test_update_resource(self):
        response = self.client.patch(
            f"/api/v1/knowledge/{self.resource_1.id}/",
            {
                "title": "Updated Django REST Framework Guide",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["title"],
            "Updated Django REST Framework Guide",
        )

    def test_delete_resource(self):
        response = self.client.delete(
            f"/api/v1/knowledge/{self.resource_1.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            KnowledgeResource.objects.filter(
                id=self.resource_1.id
            ).exists()
        )