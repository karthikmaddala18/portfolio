from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from .models import ContactMessage

class ContactViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')

    def test_contact_page_loads(self):
        """Test the contact page renders correctly"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_form_submission(self):
        """Test that submitting the form saves to DB and sends emails"""
        data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'message': 'This is a test message from the unit test suite.'
        }
        
        response = self.client.post(self.url, data)
       
        self.assertRedirects(response, self.url)
       
        self.assertEqual(ContactMessage.objects.count(), 1)
        db_message = ContactMessage.objects.first()
        self.assertEqual(db_message.name, 'Test User')
        
        self.assertEqual(len(mail.outbox), 2)
        
        admin_email = mail.outbox[0]
        self.assertIn('New Portfolio Message from Test User', admin_email.subject)
        self.assertEqual(admin_email.to, ['karthikeyamaddala3@gmail.com'])

        user_email = mail.outbox[1]
        self.assertEqual(user_email.subject, 'Message Received - Thank You!')
        self.assertEqual(user_email.to, ['testuser@example.com'])
