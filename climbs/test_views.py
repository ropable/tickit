from django.core.urlresolvers import reverse

from .models import Business, Wall, Rope, Climb
from .test_models import ClimbsTestCase as TestCase


class ClimbDetailViewTest(TestCase):

    def test_url_names(self):
        # Test named URLs can be reversed.
        for i in Climb.objects.all():
            self.assertIsNotNone(reverse('climb_detail', kwargs={'pk': i.pk}))

    def test_get(self):
        # Test response status and rendered context.
        for i in Climb.objects.all():
            url = reverse('climb_detail', kwargs={'pk': i.pk})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)