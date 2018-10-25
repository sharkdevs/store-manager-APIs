from flask import Flask, make_response, jsonify,request
from flask_restful import Resource, reqparse
from flask_jwt_extended import (jwt_required, get_jwt_identity)


from app.api.v1.models import Product, products
from app.api.v1.models import Sales, sales
from app.api.v1.models import Users, users
from app.api.v1.models import Processess


"""Required details for login"""
required = reqparse.RequestParser()
required.add_argument('email', help = "You should enter you email to login", required = True)
required.add_argument('password',help = "Password required to continue", required = True)

class Products(Resource):
    """Get the list of products in the list"""
    @jwt_required
    def get(self): 
        if get_jwt_identity() == "admin":
            if len(products)<1:
                return make_response(jsonify({
                    "Message" : "We dont have any products yet"
                }))
            else:
                return make_response(jsonify({
                    "Current User" : products
                }),200) 
        else:
            return "Only admins are allowed to post products"

    """Add a new product to the store"""
    @jwt_required
    def post(self):
        data = request.get_json()

        # create one product
        product = Product(data['product_name'],data['product_price'],data['description'],data['quantity'],data['product_image']).create_a_product()

        # add to a list and return it
        products.append(product)
        return make_response(jsonify({
            "products" : products
        }), 201)

class OneProduct(Resource):
    """Get the product by their id"""
    @jwt_required
    def get(self, id):
        self.id=id
        return Product.get_one_product(self,self.id)

class CreateSaleOrder(Resource):
    """ Making a sale order"""
    @jwt_required
    def post(self):
        return Processess.make_a_sale(self)
        
    """Get all sales orders"""
    @jwt_required
    def get(self):
        return make_response(jsonify({
            "Sales Record" : sales
        }), 200)

class GetOneSaleRecord(Resource):
    '''A get method to retrieve the sale record'''
    @jwt_required
    def get(self, id):
        return Sales.get_one_sale_record(self,id)

class UserRegistration(Resource):
    """ Register a new user"""
    def post(self):
        data = request.get_json()
        uname = data['username']
        email = data['email']
        password = data['password']
        role = data['role']
        
        user = Users(uname,email,password,role).create_user()
        users.append(user)
        return make_response(jsonify({
            "Users" : users
        }),201)

        
class UserLogin(Resource):
    def post(self):
        user = required.parse_args()
        return Users.user_login(self,user['email'],user['password'])