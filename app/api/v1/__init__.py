from flask import Flask, Blueprint
from flask_restful import Api, Resource

from app.api.v1.views import Products, OneProduct, CreateSaleOrder, GetOneSaleRecord, UserRegistration, UserLogin
v1 = Blueprint('bp',__name__,url_prefix='/api/v1')

app = Api(v1)

app.add_resource(Products,'/products')
app.add_resource(OneProduct,'/products/<int:id>')
app.add_resource( CreateSaleOrder,'/sales')
app.add_resource(GetOneSaleRecord,'/sales/<int:id>')
app.add_resource(UserRegistration, '/users/registration')
app.add_resource(UserLogin, '/users/login')