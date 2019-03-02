import unittest

from rentdynamics.client import Client


class ClientTests(unittest.TestCase):
    def test_when_development_is_false_you_get_production_url(self):
        client = Client()
        base_url = client.get_base_url()
        self.assertEqual(base_url, 'https://api.rentdynamics.com')

    def test_when_development_is_true_you_get_development_url(self):
        client = Client(development=True)
        base_url = client.get_base_url()
        self.assertEqual(base_url, 'https://api-dev.rentdynamics.com')
