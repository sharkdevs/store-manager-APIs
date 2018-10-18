from flask import Flask, make_response, jsonify
from flask_restful import Resource

from app.api.v1.models import products
class Product(Resource):
    """Get the list of products in the list"""
    def get(self):
        return make_response(jsonify({
            "products" : products
        }),200)  