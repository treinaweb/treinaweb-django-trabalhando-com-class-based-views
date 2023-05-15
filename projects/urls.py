from django.urls import path

from .views import (
    update_project,
    delete_project,
    project_details,
    ProjectListView,
    ProjectCreateView,
)

app_name = "projects"
urlpatterns = [
    path("", ProjectListView.as_view(), name="list_projects"),
    path("new/", ProjectCreateView.as_view(), name="create_project"),
    path("update/<int:pk>/", update_project, name="update_project"),
    path("delete/<int:pk>/", delete_project, name="delete_project"),
    path("details/<int:pk>/", project_details, name="project_details"),
]
