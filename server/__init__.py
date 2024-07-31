"""
Initializes the Flask server with a certain set of configurations.
"""
#dependencies
from flask import Flask
from flasgger import Swagger


#Manual config of Flask app
def create_app():
    #init app
    app = Flask(__name__)

    #register swagger
    from server.views.documentation.swagger import swagger_config, template
    swagger = Swagger(app, config=swagger_config, template=template)

    #register urls
    from .views.test import test
    app.register_blueprint(test, url_prefix="/test")

    return app
