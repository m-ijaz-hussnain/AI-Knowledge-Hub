from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from .models import KnowledgeResource
from .serializers import KnowledgeResourceSerializer


class KnowledgeResourceListCreateView(generics.ListCreateAPIView):
    """
    List existing knowledge resources or create a new resource.
    """

    queryset = KnowledgeResource.objects.all()
    serializer_class = KnowledgeResourceSerializer

    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]

    filterset_fields = [
        "resource_type",
        "is_active",
    ]

    ordering_fields = [
        "created_at",
        "updated_at",
        "published_at",
        "title",
    ]

    ordering = ["-created_at"]


class KnowledgeResourceDetailView(
    generics.RetrieveUpdateDestroyAPIView
):
    """
    Retrieve, update, or delete a knowledge resource.
    """

    queryset = KnowledgeResource.objects.all()
    serializer_class = KnowledgeResourceSerializer