from flask import Flask

#Import configurations
from instance.config import configurations

"""Function to create the app instance"""
def create_app(config_name):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(configurations[config_name])
    app.config.from_pyfile('config.py')
    
    from app.api.v1 import v1  #import the blueprint
    app.register_blueprint(v1) #register the blueprint
    
    return app