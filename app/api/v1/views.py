from flask import Flask, make_response, jsonify
from flask_restful import Resource

from app.api.v1.models import products
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