from flask import json
import unittest
import app, json

class TestStoreApp(unittest.TestCase):

    """Setup the test client"""
    def setUp(self):
        app.create_app().testing = True
        self.app = app.create_app().test_client()  

    """ Test whether the application returns and empty list"""
    def test_returns_an_empty_list(self):

        self.assertEqual(self.app.get('/api/v1/products').data, b'{"products":[]}\n')
    def test_whether_returns_status_code_on_products_query(self):
        self.assertEqual(self.app.get('/api/v1/products').status_code, 200)
    
    def test_returns_message_if_no_products(self):
        response = self.app.get('/api/v1/products')
        response = json.loads(response.data)
        assert response['Message'] == "We dont have any products yet"
