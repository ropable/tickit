#from django.contrib.auth import get_user_model
from django.test.client import Client

from django_nose import FastFixtureTestCase

from .models import Business, Wall


class ClimbsTestCase(FastFixtureTestCase):
    '''
    Defines fixtures and setup common to all model test cases.
    '''
    fixtures = [
        #'test-user.json',
        'test-business.json',
        'test-wall.json',
    ]
    cleans_up_after_itself = True

    def setUp(self):
        self.client = Client()
        self.client.login(email='ashley@ropable.com', password='test')


class BusinessModelTest(ClimbsTestCase):

    def test_unicode(self):
        '''
        Test model __unicode__() method.
        Must return a unicode string.
        '''
        for i in Business.objects.all():
            self.assertIsInstance(i.__unicode__(), unicode)


class WallModelTest(ClimbsTestCase):

    def test_unicode(self):
        '''
        Test model __unicode__() method.
        Must return a unicode string.
        '''
        for i in Wall.objects.all():
            self.assertIsInstance(i.__unicode__(), unicode)
