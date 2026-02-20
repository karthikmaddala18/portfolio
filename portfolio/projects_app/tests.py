from django.test import TestCase
from django.urls import reverse
from .models import Project

class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Test Project Alpha",
            description="Testing the project model creation process",
            tech_stack="Python, Django, Pytest",
            github_link="https://github.com/test",
            image_url="img/test.png"
        )

    def test_project_creation(self):
        self.assertEqual(self.project.title, "Test Project Alpha")
        self.assertTrue(self.project.slug) 

    def test_project_string_representation(self):
        self.assertEqual(str(self.project), "Test Project Alpha")

class ProjectViewTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Test Project Beta",
            description="Testing view functionality",
            tech_stack="JavaScript, React",
        )

    def test_project_list_view(self):
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Project Beta")
        self.assertTemplateUsed(response, 'projects.html')

    def test_project_detail_view(self):
        url = reverse('project_detail', args=[self.project.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Project Beta")
        self.assertTemplateUsed(response, 'project_detail.html')

    def test_project_detail_view_404(self):
        url = reverse('project_detail', args=['non-existent-slug'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
