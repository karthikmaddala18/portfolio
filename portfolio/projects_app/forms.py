from django import forms
from .models import Project, Certification

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'tech_stack', 'image_url', 'github_link', 'live_demo_link']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border border-slate-300 rounded focus:outline-none focus:border-blue-500'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 border border-slate-300 rounded focus:outline-none focus:border-blue-500', 'rows': 4}),
            'tech_stack': forms.TextInput(attrs={'class': 'w-full p-2 border border-slate-300 rounded focus:outline-none focus:border-blue-500', 'placeholder': 'e.g. Python, Django, React'}),
            'image_url': forms.TextInput(attrs={'class': 'w-full p-2 border border-slate-300 rounded focus:outline-none focus:border-blue-500', 'placeholder': 'URL to project image'}),
            'github_link': forms.URLInput(attrs={'class': 'w-full p-2 border border-slate-300 rounded focus:outline-none focus:border-blue-500'}),
            'live_demo_link': forms.URLInput(attrs={'class': 'w-full p-2 border border-slate-300 rounded focus:outline-none focus:border-blue-500'}),
        }

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['title', 'issuer', 'description', 'certificate_link', 'certificate_file', 'date_earned']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border border-slate-300 rounded focus:outline-none focus:border-blue-500'}),
            'issuer': forms.TextInput(attrs={'class': 'w-full p-2 border border-slate-300 rounded focus:outline-none focus:border-blue-500'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 border border-slate-300 rounded focus:outline-none focus:border-blue-500', 'rows': 4}),
            'certificate_link': forms.URLInput(attrs={'class': 'w-full p-2 border border-slate-300 rounded focus:outline-none focus:border-blue-500', 'placeholder': 'URL to view certificate online'}),
            'certificate_file': forms.FileInput(attrs={'class': 'w-full p-2 border border-slate-300 rounded focus:outline-none focus:border-blue-500'}),
            'date_earned': forms.DateInput(attrs={'type': 'date', 'class': 'w-full p-2 border border-slate-300 rounded focus:outline-none focus:border-blue-500'}),
        }
