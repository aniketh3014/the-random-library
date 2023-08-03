from cs50 import SQL
from flask import Flask, request, render_template
from helpers import random_string
import random

app = Flask(__name__)

db = SQL("sqlite:///history.db")

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET"])
def index():
    string = random_string(1000)
    print(string)
    return render_template("index.html", placeholder=string)
