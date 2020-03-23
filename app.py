# app.py

from flask import Flask

app = Flask(__name__) # if __name__ == main

@app.route("/") # When someone visits the home page, run hello function
def hello():
    return "Hello World!"

@app.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    return "About Me!"