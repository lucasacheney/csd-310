                    # Written By: Lucas Cheney
                    # For Cyber410-T301 @ Bellevue University
                    # Date: 1/14/2023
                    # Attn: Professor Haas


# MongDB Connection Module
from pymongo import MongoClient
# This was imported to deal with SSL certificate errors
import certifi                  

# Code for dealing with errors, the call is in line 17
ca = certifi.where()

# URL to MongoDB instance
url = "mongodb+srv://admin:admin@cluster1.uksh1rj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url, tlsCAFile=ca)
db = client.pytech

# Main print function
print("\n-- Pytech Collection List --")
print(db.list_collection_names())
print("\n\nEnd of program, press any key to exit...")