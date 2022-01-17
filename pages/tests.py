from django.test import TestCase
from django.test import SimpleTestCase

class SimpleTestCase(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/',follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        response = self.client.get('/about', follow=True)
        self.assertEqual(response.status_code, 200)

# Create your tests here.
