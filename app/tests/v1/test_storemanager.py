
import unittest
import app, json

class TestStoreApp(unittest.TestCase):

    """Setup the test client"""
    def setUp(self):
        app.create_app().testing = True
        self.app = app.create_app().test_client()  

    def test_whether_returns_status_code_on_products_query(self):
        self.assertEqual(self.app.get('/api/v1/products').status_code, 200)
    
    def test_returns_message_if_no_products(self):
        response = self.app.get('/api/v1/products')
        response = json.loads(response.data)
        assert response['Message'] == "We dont have any products yet"
    
    """Returns 404 if the url is malformed and does not fetch data"""
    def test_malformed_url_on_products_query(self):
        response = self.app.get('/api/v1/produc')
        self.assertEqual(response.status_code, 404)

