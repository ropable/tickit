from django.core.urlresolvers import reverse

from .models import ClimbsUser
from climbs.test_models import ClimbsTestCase as TestCase


class ClimbsUserDetailViewTest(TestCase):

    def test_url_names(self):
        # Test named URLs can be reversed.
        for i in ClimbsUser.objects.all():
            self.assertIsNotNone(reverse('climbsuser_detail', kwargs={'pk': i.pk}))

    def test_get(self):
        # Test response status and rendered context.
        for i in ClimbsUser.objects.all():
            url = reverse('climbsuser_detail', kwargs={'pk': i.pk})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_get_content(self):
        # Test response contains the expected content.
        for i in ClimbsUser.objects.all():
            url = reverse('climbsuser_detail', kwargs={'pk': i.pk})
            response = self.client.get(url)
            self.assertContains(response, '<p>Email: {}</p>'.format(i.email))
