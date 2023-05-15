from django.urls import path

from .views import (
    delete_project,
    project_details,
    ProjectListView,
    ProjectCreateView,
    ProjectUpdateView,
)

app_name = "projects"
urlpatterns = [
    path("", ProjectListView.as_view(), name="list_projects"),
    path("new/", ProjectCreateView.as_view(), name="create_project"),
    path("update/<int:pk>/", ProjectUpdateView.as_view(), name="update_project"),
    path("delete/<int:pk>/", delete_project, name="delete_project"),
    path("details/<int:pk>/", project_details, name="project_details"),
]
