                            #Written By: Lucas Cheney
                            # For CYBR410-T301 @ Bellevue University
                            # Date 1/22/2023
                            # Attn: Professor Haas

# Modules to connect to MongoDB
from pymongo import MongoClient
import certifi

# Deals with certificate errors during communication with server
ca = certifi.where()

# Connection to MongoDB collection
url = "mongodb+srv://admin:admin@cluster1.uksh1rj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url, tlsCAFile=ca)
db = client.pytech

# Call to students db
students = db.students
student_list = students.find()

# Print students db
print("\n\n -- DISPLAYING STUDENTS FROM find() QUERY --")
for doc in student_list: 
    print("\n Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# Changing last name of student id_1007
students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})

# Print to terminal to ensure success of change
rebeka = db.students.find_one({"student_id":"1007"})
print("\n\n -- DISPLAYING STUDENT FROM find_one() QUERY --")
print("\n Student ID: " + rebeka["student_id"] + "\n First Name: " + rebeka["first_name"] + "\n Last Name: " + rebeka["last_name"])

# End of program
input("\n\n End of program, press any key to continue...")