from django.urls import path
from django.views.generic import RedirectView

app_name = "core"
urlpatterns = [
    path("", RedirectView.as_view(pattern_name="projects:list_projects"), name="home"),
]
