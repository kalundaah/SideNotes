"""
Initializes the Flask server with a certain set of configurations.
"""
# dependencies
import json
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from models.engine import DATABASE_URL

try:
    load_dotenv(".env")
except FileNotFoundError:
    print("No .env file found. Using default config")

# Server extensions
db = SQLAlchemy()
migrate = Migrate()

# Manual config of Flask app
def create_app():
    # init app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    SWAGGER_URL = '/api/docs'
    API_URL = "/swagger.json"

    swaggerui_blueprint = get_swaggerui_blueprint(
        base_url=SWAGGER_URL,
        api_url=API_URL,
        config={
            'app_name': 'Sidenotes Swagger',
        }
    )

    # Initializing extentions
    db.init_app(app)
    migrate.init_app(app, db)


    app.register_blueprint(blueprint=swaggerui_blueprint,
                           url_prefix=SWAGGER_URL)

    @app.route('/swagger.json')
    def swagger():
        with open('server/views/Documentation/swagger.json', 'r') as f:
            return jsonify(json.load(f))

    # register urls
    from .views.general import general
    app.register_blueprint(general, url_prefix='')
    from .views.note import note
    app.register_blueprint(note, url_prefix="/note")

    print("app fully generated")
    return app
