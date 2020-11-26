from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/Mars_db")

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    articles_images = mongo.db.articles_images.find_one()
    print(articles_images)

    # Return template and data
    return render_template("index.html", articles_images=articles_images)

# Route that will trigger the scrape function
@app.route('/scrape')
def scrape():
    articles_images = mongo.db.articles_images
    data = scrape_mars.scrape_all()
    articles_images.update({}, data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
