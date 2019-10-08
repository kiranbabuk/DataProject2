import pymongo



client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0-hsqne.gcp.mongodb.net/admin?retryWrites=true&w=majority")
db = client['airbnb']

print(db.list_collection_names())