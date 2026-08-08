from rest_framework import generics

from .models import KnowledgeResource
from .serializers import KnowledgeResourceSerializer


class KnowledgeResourceListCreateView(generics.ListCreateAPIView):
    """
    List existing knowledge resources or create a new resource.
    """

    queryset = KnowledgeResource.objects.all()
    serializer_class = KnowledgeResourceSerializer


class KnowledgeResourceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a knowledge resource.
    """

    queryset = KnowledgeResource.objects.all()
    serializer_class = KnowledgeResourceSerializer