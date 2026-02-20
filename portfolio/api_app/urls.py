from django.urls import path
from . import views

urlpatterns = [
 
    path('projects/', views.ProjectListAPIView.as_view(), name='api_project_list'),
    path('projects/<slug:slug>/', views.ProjectDetailAPIView.as_view(), name='api_project_detail'),
    

    path('contact/', views.ContactCreateAPIView.as_view(), name='api_contact_create'),
]