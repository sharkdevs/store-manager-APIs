from flask import Flask, make_response, jsonify,request
from flask_restful import Resource

from app.api.v1.models import Product as p, products
from app.api.v1.models import Sales as s, sales
from app.api.v1.models import Users as U, users
from app.api.v1.models import Processess

class Products(Resource):
    """Get the list of products in the list"""
    def get(self): 
        if len(products)<1:
            return make_response(jsonify({
                "Message" : "We dont have any products yet"
            }))
        else:
            return make_response(jsonify({
                "products" : products
            }),200) 

    """Add a new product to the store"""
    def post(self):
        data = request.get_json()

        # create one product
        product = p(data['product_name'],data['product_price'],data['description'],data['quantity'],data['product_image']).create_a_product()

        # add to a list and return it
        products.append(product)
        return make_response(jsonify({
            "products" : products
        }), 201)

class OneProduct(Resource):
    """Get the product by their id"""
    def get(self, id):
        self.id=id
        return p.get_one_product(self,self.id)

class CreateSaleOrder(Resource):
    """ Making a sale order"""
    def post(self):
        return Processess.make_a_sale(self)
        
    """Get all sales orders"""
    def get(self):
        return make_response(jsonify({
            "Sales Record" : sales
        }), 200)

class GetOneSaleRecord(Resource):
    '''A get method to retrieve the sale record'''
    def get(self, id):
        return s.get_one_sale_record(self,id)

class UserRegistration(Resource):
    """ Register a new user"""
    def post(self):
        data = request.get_json()
        uname = data['username']
        email = data['email']
        password = data['password']
        role = data['role']
        
        user = U(uname,email,password,role).create_user()
        users.append(user)
        return make_response(jsonify({
            "Users" : users
        }),201)
class UserLogin(Resource):
    def post(self):
        return make_response(jsonify({
            "Login" : "User login"
        }))