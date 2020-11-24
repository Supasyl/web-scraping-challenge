from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/Mars_db")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    collection = mongo.db.collection.find_one()
    # Return template and data
    return render_template("index.html", collection=collection)

    # Find the feature image from the mongo database
    images = mongo.db.images.find()
    # Return template and data
    return render_template("index.html", images=images)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    collection = mongo.db.collection
    article = scrape_mars.scrape_info()
    # Update the Mongo database using update and upsert=True
    collection.update({}, article, upsert=True)

    # Run the scrape function
    images = mongo.db.images
    feature_image_url = scrape_mars.scrape_info2()
    # Update the Mongo database using update and upsert=True
    images.update({}, feature_image_url, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)






# # Define database and collection
# db = client.Mars_db
# collection = db.articles
# images = db.images
#     # Insert dictionary into MongoDB as a document
#         collection.insert_one(post)
# # Display items in MongoDB collection
# list = db.articles.find()

# for listing in list:
#     print(listing)

# images.insert_one(post)
