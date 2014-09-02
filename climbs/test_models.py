from django.contrib.auth import get_user_model
from django.db import transaction
from django.test.client import Client

from django_nose import FastFixtureTestCase

from .models import Business, Wall, Rope, Climb

USER = get_user_model()


class ClimbsTestCase(FastFixtureTestCase):
    '''
    Defines fixtures and setup common to all model test cases.
    '''
    fixtures = [
        'test-business.json',
        'test-wall.json',
        'test-rope.json',
        'test-climb.json',
    ]
    cleans_up_after_itself = True

    @classmethod
    def setUpClass(cls):
        transaction.set_autocommit(True)
        if USER.objects.filter(email='ashley@ropable.com').exists():
            cls.user = USER.objects.filter(email='ashley@ropable.com')
        else:
            cls.user = USER.objects.create_user(
                email='ashley@ropable.com',
                password='test'
            )
        transaction.set_autocommit(False)

    @classmethod
    def tearDownClass(cls):
        transaction.set_autocommit(True)
        u = USER.objects.get(email='ashley@ropable.com')
        u.delete()
        transaction.set_autocommit(False)

    def setUp(self):
        self.client = Client()


class BusinessModelTest(ClimbsTestCase):

    def test_unicode(self):
        '''
        Test model __unicode__() method. Must return a unicode string.
        '''
        for i in Business.objects.all():
            self.assertIsInstance(i.__unicode__(), unicode)


class WallModelTest(ClimbsTestCase):

    def test_unicode(self):
        '''
        Test model __unicode__() method. Must return a unicode string.
        '''
        for i in Wall.objects.all():
            self.assertIsInstance(i.__unicode__(), unicode)


class RopeModelTest(ClimbsTestCase):

    def test_unicode(self):
        '''
        Test model __unicode__() method. Must return a unicode string.
        '''
        for i in Rope.objects.all():
            self.assertIsInstance(i.__unicode__(), unicode)


class ClimbModelTest(ClimbsTestCase):

    def test_unicode(self):
        '''
        Test model __unicode__() method. Must return a unicode string.
        '''
        for i in Climb.objects.all():
            self.assertIsInstance(i.__unicode__(), unicode)
