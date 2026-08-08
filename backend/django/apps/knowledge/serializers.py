from rest_framework import serializers

from .models import KnowledgeResource


class KnowledgeResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeResource
        fields = (
            "id",
            "title",
            "description",
            "resource_type",
            "source_url",
            "author",
            "published_at",
            "is_active",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )