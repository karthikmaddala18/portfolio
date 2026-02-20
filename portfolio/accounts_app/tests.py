from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from projects_app.models import Project

class AccountsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.project = Project.objects.create(
            title="Test Home Project",
            description="Testing home page display",
            tech_stack="Python",
        )

    def test_home_page_loads(self):
        """Test home page renders properly"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, "Karthikeya")

    def test_about_page_loads(self):
        """Test about page renders properly"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_dashboard_access_denied_for_anonymous(self):
        """Test dashboard requires login"""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302) 
        self.assertIn('/login/', response.url)

    def test_dashboard_access_allowed_for_logged_in(self):
        """Test dashboard renders for authenticated users"""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
        self.assertContains(response, "User Dashboard")
