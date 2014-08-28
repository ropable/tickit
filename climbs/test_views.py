from django.core.urlresolvers import reverse
from django.test.client import Client

#from .models import Business, Wall
from .test_models import ClimbsTestCase as TestCase


class ClimbDetailViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        url = reverse('climb_detail')
        self.response = self.client.get(url)

    def test_url_names(self):
        # Test named URLs can be reversed.
        self.assertIsNotNone(reverse('climb_detail'))

    def test_get(self):
        # Test response status and rendered context.
        self.assertEqual(self.response.status_code, 200)
