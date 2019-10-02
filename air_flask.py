from flask import Flask, render_template
import pymongo

app = Flask(__name__)

conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)

db = client.airbnb

@app.route("/")
def data():
    locales = list(db.nyc_locations.find())
    print(locales)
    return render_template('index.html', locales=locales)

if __name__ == "__main__":
    app.run(debug=True)
