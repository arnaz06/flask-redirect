

from app import app, redirect, scrape, jsonify


@app.route("/")
def move():
  return redirect('http://go-jek.com/'+scrape()+'/')
