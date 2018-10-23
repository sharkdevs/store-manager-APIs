from flask import Flask
from flask_jwt_extended import JWTManager

#Import configurations
from instance.config import app_config, Config

"""Function to create the app instance"""
def create_app(config_name):
    app = Flask(__name__,instance_relative_config=True)
    
    # app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['JWT_SECRET_KEY'] = "meshack-secret"
    jwt = JWTManager(app)

    from app.api.v1 import v1  #import the blueprint
    app.register_blueprint(v1) #register the blueprint
    
    return app