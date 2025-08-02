from flask import Blueprint

# Create the blueprin object
# the first argument is the blueprint name
# the second argument is the import name
routes = Blueprint('routes', __name__)

# Create a route
@routes.route('/')
def index():
    return 'Hello, World!'