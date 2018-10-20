from flask import Flask

"""Function to create the app instance"""
def create_app(test_config):
    app = Flask(__name__,instance_relative_config=True)

    #set the secret key
    app.config.from_mapping(
        SECRET_KEY = "Mesh"
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    from app.api.v1 import v1  #import the blueprint
    app.register_blueprint(v1) #register the blueprint
    
    return app