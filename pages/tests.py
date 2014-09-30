from django.test import TestCase
#from django_nose import FastFixtureTestCase as TestCase


class HomePageTest(TestCase):

    def test_root_url_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
