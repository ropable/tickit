from django.test import TestCase


class HomePageTest(TestCase):

    def test_root_url_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
