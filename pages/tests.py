from django.test import TestCase

# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_url_by_name(self):
        response=self.client.get(reversed('home'))
        self.assertEqual((response.status_code,200))

    def test_home_page_url_by_name(self):
        response=self.client.get(reversed('home'))
        self.assertEqual((response.status_code,200))