from django.urls import path

from .views import (
    ProjectListView,
    ProjectCreateView,
    ProjectUpdateView,
    PorjectDetailView,
    ProjectDeleteView,
)

app_name = "projects"
urlpatterns = [
    path("", ProjectListView.as_view(), name="list_projects"),
    path("new/", ProjectCreateView.as_view(), name="create_project"),
    path("update/<int:pk>/", ProjectUpdateView.as_view(), name="update_project"),
    path("delete/<int:pk>/", ProjectDeleteView.as_view(), name="delete_project"),
    path("details/<int:pk>/", PorjectDetailView.as_view(), name="project_details"),
]
