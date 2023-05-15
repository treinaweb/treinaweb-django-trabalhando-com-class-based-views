from django.urls import path

from .views import (
    list_projects,
    create_project,
    update_project,
    delete_project,
    project_details,
)

app_name = "projects"
urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("new/", create_project, name="create_project"),
    path("update/<int:pk>/", update_project, name="update_project"),
    path("delete/<int:pk>/", delete_project, name="delete_project"),
    path("details/<int:pk>/", project_details, name="project_details"),
]
