from flask import Flask
from .routes import routes

# Create the app instance
def create_app():
    app = Flask(__name__)
    # Register the blueprints
    app.register_blueprint(routes)
    return app