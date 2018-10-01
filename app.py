from flask import Flask, redirect
from scrape import scrape

app= Flask(__name__)

@app.route("/")
def index():
  return redirect('http://go-jek.com/'+scrape()+'/')


if __name__ == "__main__":
  app.run()
