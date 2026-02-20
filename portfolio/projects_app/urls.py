from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('create/', views.project_create, name='project_create'),
    path('certifications/create/', views.certification_create, name='certification_create'),
    path('certifications/<int:pk>/delete/', views.certification_delete, name='certification_delete'),
    path('<slug:slug>/', views.project_detail, name='project_detail'),
    path('<slug:slug>/delete/', views.project_delete, name='project_delete'),
]