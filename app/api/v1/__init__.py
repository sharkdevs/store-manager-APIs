from flask import Flask, Blueprint
from flask_restful import Api, Resource

from app.api.v1.views import Products, OneProduct
v1 = Blueprint('bp',__name__,url_prefix='/api/v1')

app = Api(v1)

app.add_resource(Products,'/products')
app.add_resource(OneProduct,'/products/<int:id>')