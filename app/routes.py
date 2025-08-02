from flask import Blueprint, render_template

# Create the blueprin object
# the first argument is the blueprint name
# the second argument is the import name
routes = Blueprint('routes', __name__)

# Create a route
@routes.route('/')
def index():
    return render_template('home.html')

@routes.route('/about')
def about():
    pass

@routes.route('/subscribe')
def subscribe():
    pass

@routes.route('/contact')
def contact():
    pass