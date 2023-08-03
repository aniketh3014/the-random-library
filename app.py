from cs50 import SQL
from flask import Flask, request, render_template
from helpers import random_string
import random

app = Flask(__name__)

db = SQL("sqlite:///history.db")

