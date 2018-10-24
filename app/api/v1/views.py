from flask import Flask, make_response, jsonify,request
from flask_restful import Resource

from app.api.v1.models import Product as p, products
from app.api.v1.models import Sales as s, sales
from app.api.v1.models import Users as U, users

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
        data = request.get_json()
        s_id = data['sales_id']
        p_id = data['product_id']
        quant = data['quantity']
        s_amt = data['sales_amount']
        s_date = data['sales_date']

        #check whether the product is in store and in stock
        for product in products:
            if product['product_id']==p_id and product['quantity']>quant:
                # create one sale order
                sale = s(s_id,p_id,quant,s_amt,s_date).make_a_sale()

                # add to the sales list and return it
                sales.append(sale)
                return make_response(jsonify({
                    "sales" : sales
                }), 201)
            else:
                return make_response(jsonify({ "Message" : "Product requested not in store"}),404)

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
