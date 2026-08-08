from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from .serializers import HealthCheckSerializer


class HealthCheckView(APIView):
    """
    Health check endpoint for the Django API service.
    """

    authentication_classes = []
    permission_classes = []

    @extend_schema(
        responses=HealthCheckSerializer,
        description="Returns the current health status of the Django API service.",
    )
    def get(self, request):
        return Response(
            {
                "status": "ok",
                "service": "django-api",
            }
        )