from django.db import models


class KnowledgeResource(models.Model):
    class ResourceType(models.TextChoices):
        ARTICLE = "article", "Article"
        PAPER = "paper", "Research Paper"
        DOCUMENTATION = "documentation", "Documentation"
        TUTORIAL = "tutorial", "Tutorial"
        VIDEO = "video", "Video"
        COURSE = "course", "Course"

    title = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    resource_type = models.CharField(
        max_length=30,
        choices=ResourceType.choices,
    )

    source_url = models.URLField(max_length=500)

    author = models.CharField(
        max_length=255,
        blank=True,
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["resource_type"]),
            models.Index(fields=["is_active"]),
            models.Index(fields=["-created_at"]),
        ]

    def __str__(self):
        return self.title