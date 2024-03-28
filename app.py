from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("templates/index.html", message="Hello!")
