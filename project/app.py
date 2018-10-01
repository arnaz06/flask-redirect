
from flask import Flask, jsonify, redirect, url_for
from flask_frozen import Freezer
from scrape import scrape

app = Flask(__name__)
app.config.from_pyfile('settings.py')
freezer = Freezer(app)
