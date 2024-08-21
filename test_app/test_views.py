from django.test import TestCase
from django.urls import reverse_lazy

# reverse_lazy('contact')

class ContactViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('contact')
        return super().setUpClass()
    
    def test_url(self):
        self.assertEqual(self.url, '/en/contact-us/')

    def test_response_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)

    def test_response_context(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'contact.html')
    
    @classmethod
    def tearDownClass(cls) -> None:
        pass