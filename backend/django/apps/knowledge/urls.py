from django.urls import path

from .views import (
    KnowledgeResourceDetailView,
    KnowledgeResourceListCreateView,
)

app_name = "knowledge"

urlpatterns = [
    path(
        "",
        KnowledgeResourceListCreateView.as_view(),
        name="resource-list-create",
    ),
    path(
        "<int:pk>/",
        KnowledgeResourceDetailView.as_view(),
        name="resource-detail",
    ),
]