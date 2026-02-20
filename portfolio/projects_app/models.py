from django.db import models
from django.utils.text import slugify

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True) 
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200, blank=True, default='')
    github_link = models.URLField(blank=True)
    live_demo_link = models.URLField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, help_text="Link to GitHub repository (optional)")
    certificate_link = models.URLField(blank=True, help_text="Link to online certificate (optional)")
    certificate_file = models.FileField(upload_to='certifications/', blank=True, null=True, help_text="Upload certificate file (PDF/Image)")
    date_earned = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.issuer}"