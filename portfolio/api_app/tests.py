from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from projects_app.models import Project
from contact_app.models import ContactMessage
from django.contrib.auth.models import User

class APIEndpointsTest(APITestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="API Test Project",
            description="Testing the API views",
            tech_stack="Django REST Framework",
        )
        self.user = User.objects.create_user(username='testadmin', password='testpassword')

    def test_get_project_list(self):
        """Test retrieving list of projects via API"""
        url = reverse('api_project_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertGreaterEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "API Test Project")

    def test_get_project_detail(self):
        """Test retrieving single project via API"""
        url = reverse('api_project_detail', args=[self.project.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "API Test Project")

    def test_create_project_unauthorized(self):
        """Test creating project without auth fails"""
        url = reverse('api_project_list')
        data = {'title': 'New Project', 'description': 'desc', 'tech_stack': 'tech'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_project_authorized(self):
        """Test creating project with auth succeeds"""
        self.client.login(username='testadmin', password='testpassword')
        url = reverse('api_project_list')
        data = {'title': 'New API Project', 'description': 'desc', 'tech_stack': 'tech'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 2)

    def test_create_contact_message(self):
        """Test creating a contact message via API"""
        url = reverse('api_contact_create')
        data = {
            'name': 'API User',
            'email': 'api@test.com',
            'subject': 'API Test',
            'message': 'Hello from API tests'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactMessage.objects.first().name, 'API User')
