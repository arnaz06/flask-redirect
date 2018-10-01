from flask_frozen import Freezer
from flask import Flask, jsonify, redirect, url_for
from scrape import scrape

app = Flask(__name__)
freezer= Freezer(app)

@app.route("/")
def index():
    return redirect('http://go-jek.com/'+scrape()+'/')
@app.route("/coba")
def coba():
  return jsonify({"about":"redirected"})
if __name__== '__main__':
  freezer.freezer()

