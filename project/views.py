

from app import app, redirect, scrape, jsonify


@app.route("/")
def hello():
  return jsonify({"description":"go to /move"})

@app.route("/move")
def move():
  return redirect('http://go-jek.com/'+scrape()+'/')
