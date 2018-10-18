from flask import Flask, Blueprint
from flask_restful import Api, Resource

v1 = Blueprint('bp',__name__,url_prefix='/api/v1')

app = Api(v1)

