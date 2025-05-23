from flask import Flask
import requests
import numpy as np

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Render!"
