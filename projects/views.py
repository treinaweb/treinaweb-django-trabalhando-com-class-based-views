from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.urls import reverse_lazy

from .models import Project


class ProjectListView(ListView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Lista de Projetos"
        return context


class ProjectCreateView(CreateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("projects:list_projects")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Criar Projeto"
        return context


class ProjectUpdateView(UpdateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("projects:list_projects")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Editar Projeto"
        return context


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy("projects:list_projects")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Deletar Projeto"
        return context


class PorjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Detalhes do Projeto"
        return context
