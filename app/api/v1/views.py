from flask import Flask, make_response, jsonify,request
from flask_restful import Resource

from app.api.v1.models import Product as p, products
from app.api.v1.models import Sales as s, sales

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

        # create one sale order
        sale = s(data['sales_id'],data['product_id'],data['quantity'],data['sales_amount'],data['sales_date']).make_a_sale()

        # add to the sales list and return it
        sales.append(sale)
        return make_response(jsonify({
            "sales" : sales
        }), 201)