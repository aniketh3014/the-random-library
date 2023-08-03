from cs50 import SQL
from flask import Flask, request, render_template
from helpers import random_string
import random

app = Flask(__name__)

db = SQL("sqlite:///history.db")

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        page = request.form.get("page")
    string = random_string(1000)
    return render_template("index.html", string=string, name ="Aniket")
