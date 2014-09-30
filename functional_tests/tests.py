from django.test import LiveServerTestCase
from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_visit_home_page(self):
        self.browser.get(self.live_server_url)
        assert 'Climbing, shared.' in self.browser.page_source
