from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def home1():
    return 'Hi there'



if __name__ == "__main__":
    app.run(debug=True)