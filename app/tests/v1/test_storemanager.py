import unittest

import app

class TestStoreApp(unittest.TestCase):

    """Setup the test client"""
    def setUp(self):
        app.create_app().testing = True
        self.app = app.create_app().test_client() 

    """ Test whether the application returns and empty list"""
    def test_returns_an_empty_list(self):
        
        self.assertEqual(self.app.get('/api/v1/products').data, [])
