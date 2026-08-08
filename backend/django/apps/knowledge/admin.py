from django.contrib import admin

from .models import KnowledgeResource


@admin.register(KnowledgeResource)
class KnowledgeResourceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "resource_type",
        "author",
        "is_active",
        "published_at",
        "created_at",
    )

    list_filter = (
        "resource_type",
        "is_active",
    )

    search_fields = (
        "title",
        "description",
        "author",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )