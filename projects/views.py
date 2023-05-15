from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView
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


def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects:list_projects")
    return render(
        request,
        "projects/delete_project.html",
        {"page_title": "Deletar Projeto", "project": project},
    )


class PorjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Detalhes do Projeto"
        return context
