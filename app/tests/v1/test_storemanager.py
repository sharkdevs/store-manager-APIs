
import unittest
import app, json

class TestStoreApp(unittest.TestCase):

    """Setup the test client"""
    def setUp(self):
        app.create_app().testing = True
        self.app = app.create_app().test_client() 

        '''This data shall be used for testing purposes'''
        self.sample_data = {
            "product_id" : 1,
            "product_name" : "Soap",
            "product_price" : 450,
            "description" : "Jamaa soap Utapenda",
            "quantity" : 30,
            "product_image" : "image/d.jpg"
        } 

    def test_whether_returns_status_code_on_products_query(self):
        self.assertEqual(self.app.get('/api/v1/products').status_code, 200)
    
    def test_returns_message_if_no_products(self):
        response = self.app.get('/api/v1/products')
        assert response.status_code == 200
    
    """Returns 404 if the url is malformed and does not fetch data"""
    def test_malformed_url_on_products_query(self):
        response = self.app.get('/api/v1/produc')
        self.assertEqual(response.status_code, 404)

    def test_adds_a_new_product(self):
        response = self.app.post('/api/v1/products', data = json.dumps(self.sample_data), content_type='application/json')
        self.assertEqual(response.status_code,201)
