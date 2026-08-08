from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import KnowledgeResource


class KnowledgeResourceAPITests(APITestCase):
    def setUp(self):
        self.resource = KnowledgeResource.objects.create(
            title="Attention Is All You Need",
            description="Research paper introducing the Transformer architecture.",
            resource_type=KnowledgeResource.ResourceType.PAPER,
            source_url="https://arxiv.org/abs/1706.03762",
            author="Vaswani et al.",
            is_active=True,
        )

    def test_list_resources_returns_200(self):
        response = self.client.get(
            reverse("knowledge:resource-list-create")
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_list_resources_returns_created_resource(self):
        response = self.client.get(
            reverse("knowledge:resource-list-create")
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data[0]["title"],
            self.resource.title,
        )

    def test_create_resource_returns_201(self):
        payload = {
            "title": "Django REST Framework",
            "description": "Toolkit for building Web APIs with Django.",
            "resource_type": KnowledgeResource.ResourceType.DOCUMENTATION,
            "source_url": "https://www.django-rest-framework.org/",
            "author": "",
            "is_active": True,
        }

        response = self.client.post(
            reverse("knowledge:resource-list-create"),
            payload,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(
            KnowledgeResource.objects.count(),
            2,
        )

    def test_retrieve_resource_returns_200(self):
        response = self.client.get(
            reverse(
                "knowledge:resource-detail",
                kwargs={"pk": self.resource.pk},
            )
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            response.data["title"],
            self.resource.title,
        )

    def test_update_resource_returns_200(self):
        payload = {
            "title": "Updated Knowledge Resource",
            "description": self.resource.description,
            "resource_type": self.resource.resource_type,
            "source_url": self.resource.source_url,
            "author": self.resource.author,
            "published_at": self.resource.published_at,
            "is_active": self.resource.is_active,
        }

        response = self.client.put(
            reverse(
                "knowledge:resource-detail",
                kwargs={"pk": self.resource.pk},
            ),
            payload,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            response.data["title"],
            "Updated Knowledge Resource",
        )

    def test_delete_resource_returns_204(self):
        response = self.client.delete(
            reverse(
                "knowledge:resource-detail",
                kwargs={"pk": self.resource.pk},
            )
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            KnowledgeResource.objects.filter(
                pk=self.resource.pk
            ).exists()
        )