from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from projects_app.models import Project, Certification 

def home(request):
   
    projects = Project.objects.all().order_by('-created_date')[:3]
    return render(request, 'home.html', {'projects': projects})

def about(request):
    certifications = Certification.objects.all().order_by('id')
    return render(request, 'about.html', {'certifications': certifications})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def dashboard(request):
    
    projects = Project.objects.all().order_by('-created_date')
    certifications = Certification.objects.all().order_by('-date_earned')
    return render(request, 'dashboard.html', {'projects': projects, 'certifications': certifications})