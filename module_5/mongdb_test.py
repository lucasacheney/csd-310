from pymongo import MongoClient
import certifi

ca = certifi.where()
url = "mongodb+srv://admin:admin@cluster1.uksh1rj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url, tlsCAFile=ca)
db = client.pytech

print("\n-- Pytech Collection List --")
print(db.list_collection_names())
print("\n\nEnd of program, press any key to exit...")