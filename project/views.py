

from app import app, redirect, scrape, jsonify

@app.route("/")
def index():
    return jsonify({'about':'ulala'})
    

@app.route("/move")
def move():
  return redirect('http://go-jek.com/'+scrape()+'/')
