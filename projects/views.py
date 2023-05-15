from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, CreateView
from django.urls import reverse_lazy

from .models import Project
from .forms import ProjectForm


class ProjectListView(ListView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Lista de Projetos"
        return context


class CreateProjectView(View):
    def get(self, request):
        return render(
            request,
            "projects/form_project.html",
            {"page_title": "Criar Projeto", "form": ProjectForm()},
        )

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("projects:list_projects")
        return render(
            request,
            "projects/form_project.html",
            {"page_title": "Criar Project", "form": form},
        )


class ProjectCreateView(CreateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("projects:list_projects")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Criar Projeto"
        return context


def update_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect("projects:list_projects")
    return render(
        request,
        "projects/form_project.html",
        {"page_title": "Editar Projeto", "form": form},
    )


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


def project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(
        request,
        "projects/project_details.html",
        {"page_title": "Detalhes do Projeto", "project": project},
    )
