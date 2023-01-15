                    # Title: pytech_queries.py
                    # Written By: Lucas Cheney
                    # For Cyber410-T301 @ Bellevue University
                    # Date: 1/15/2023
                    # Attn: Professor Haas
                    # Description: Call to students DB


# MongDB Connection Module
from pymongo import MongoClient
# This was imported to deal with SSL certificate errors
import certifi                  

# Code for dealing with errors, the call is in line 19
ca = certifi.where()

# Call to MongoDB database
url = "mongodb+srv://admin:admin@cluster1.uksh1rj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url, tlsCAFile=ca)
db = client.pytech
students = db.students
student_list = students.find({})


print("\n\n -- DISPLAYING STUDENTS FROM find() QUERY --")
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: "+ doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")


alexis = db.students.find_one({"student_id":"1008"})     
print("\n\n -- DISPLAYING STUDENT FROM find_one() QUERY --")
print(" Student ID: " + alexis["student_id"] + "\n First Name: " + alexis["first_name"] + "\n Last Name: " + alexis["last_name"] + "\n")

input("\n\n End of program, press any key to continue...")