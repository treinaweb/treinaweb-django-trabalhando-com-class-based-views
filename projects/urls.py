from django.urls import path

from .views import (
    list_projects,
    update_project,
    delete_project,
    project_details,
    CreateProjectView,
)

app_name = "projects"
urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("new/", CreateProjectView.as_view(), name="create_project"),
    path("update/<int:pk>/", update_project, name="update_project"),
    path("delete/<int:pk>/", delete_project, name="delete_project"),
    path("details/<int:pk>/", project_details, name="project_details"),
]
