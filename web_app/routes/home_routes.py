# web_app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes",__name__)

@app.routes.route("/") # When someone visits the home page, run hello function
def hello():
    return "Hello World!"

@app.routes.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    return "About Me!"