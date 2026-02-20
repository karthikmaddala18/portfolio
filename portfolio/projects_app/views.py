from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Certification
from .forms import ProjectForm, CertificationForm

# Create your views here.

def project_list(request):
    projects = Project.objects.all().order_by('-created_date')
    return render(request, 'projects.html', {'projects': projects})

def project_detail(request, slug):
  
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
     
            return redirect('project_detail', slug=project.slug)
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})

@login_required
def project_delete(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'project_confirm_delete.html', {'project': project})

@login_required
def certification_create(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('dashboard')
    else:
        form = CertificationForm()
    return render(request, 'certification_form.html', {'form': form})

@login_required
def certification_delete(request, pk):
    certification = get_object_or_404(Certification, pk=pk)
    if request.method == 'POST':
        certification.delete()
        return redirect('dashboard')
    return render(request, 'certification_confirm_delete.html', {'certification': certification})