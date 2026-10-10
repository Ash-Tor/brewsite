from flask import Flask
from flask import render_template as rt

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return rt("home.html", user = "Ashley Torres")

@app.route("/breweries")
def breweries():
	return rt("breweries.html", user = "Ashley Torres")

@app.route("/beer_types")
def beer_types():
	return rt("beer_types.html", user = "Ashley Torres")

@app.route("/about")
def about():
	return rt("about.html", user = "Ashley Torres")




if __name__ == "__main__":
	app.run(debug=True)