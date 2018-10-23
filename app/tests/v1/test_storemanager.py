from flask import jsonify


import unittest
import app, json

from app.api.v1.models import products
from app import create_app
from app.tests.v1.models import TestData
class TestStoreApp(unittest.TestCase):

    """Setup the test client"""
    def setUp(self):
        test_app = create_app(config_name='testing')
        self.app = test_app.test_client() 

        '''Import all the data to be used for users'''
        self.sample_data = TestData.sample_data
        self.sample_sales_data = TestData.sample_sales_data
        self.sample_user = TestData.sample_user

        

        products.append(self.sample_data)
        
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

    def test_malformed_post_one_product_url(self):
        response = self.app.post('/api/v1/products//', data = json.dumps(self.sample_data), content_type='application/json')
        self.assertEqual(response.status_code,404)
    
    '''Test whether the api fetches a product successfull'''
    def test_get_a_product_by_id(self):
        response = self.app.get('/api/v1/products/1')
        self.assertEqual(response.status_code,200)

    def test_malformed_url_on_a_given_product_query_by_id(self):
        response = self.app.get('/api/v1/products/1/wsd')
        self.assertEqual(response.status_code,404)
    
    '''Returns a message if the id is ou of bounds'''
    def test_gives_error_feedback_if_product_id_out_of_bounds(self):
        response = self.app.get('/api/v1/products/0')
        res = json.loads(response.data)
        self.assertEqual(res['Message'],"The product requested is not in store") 

    def test_adds_a_new_sale_order_successfully(self):
        products.append(self.sample_data)
        response = self.app.post(
            '/api/v1/sales', 
            data = json.dumps(self.sample_sales_data), 
            content_type='application/json'
            )
        self.assertEqual(response.status_code,201)

    '''Gives feedback if the product isout of stock'''
    def test_gives_Alert_feedback_if_product_not_in_stock(self):
        products.append(self.sample_data)
        self.sample_sales_data['quantity']=80 #make the quantity more than stock
        feedback = self.app.post(
            '/api/v1/sales', 
            data = json.dumps(self.sample_sales_data), 
            content_type='application/json'
            )
        res = json.loads(feedback.data)
        self.assertEqual(res['Message'],"Product requested not in store") 

    """A test to check whether sales are returned successfull"""
    def test_return_all_sales_orders(self):
        self.assertEqual(self.app.get('/api/v1/sales').status_code, 200)
    
    '''Test whether a malformed url gives an error'''
    def test_malformed_url_for_get_all_products(self):
        response = self.app.get('/api/v1/saleswsd')
        self.assertEqual(response.status_code,404)

    '''Test to see whether returns a specific sales order'''
    def test_gets_one_sales_order_by_id(self):
        response = self.app.get('/api/v1/sales/1')
        self.assertEqual(response.status_code,200)
    
    """Test user registration"""
    def test_adds_a_new_user(self):
        response = self.app.post('/api/v1/users/registration', data = json.dumps(self.sample_user), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    #def test_user_login(self):
        #self.assertEqual(self.app.post('/api/v1/users/login').status_code, 200)