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

# New student doc
kasey = {
    "student_id": "1010",
    "first_name": "Kasey",
    "last_name": "Cheney"
}

# Insert new document into db
kasey_student_id = students.insert_one(kasey).inserted_id

# Notification of inserted document
print("\n -- INSERTED DOCUMENT --")
print(" Inserted student record with document_id " + str(kasey_student_id))

# Find newly created document
kasey = students.find_one({"student_id": "1010"})

# Display the record
print("\n -- DISPLAYING DOCUMENT --")
print(" Student ID: " + kasey["student_id"] + "\n First Name: " + kasey["first_name"] + "\n Last Name: " + kasey["last_name"] + "\n")

# Delete the newly created student document
delete_kasey_student = students.delete_one({"student_id": "1010"})

# Call students to ensure deletion
new_student_list = students.find({})

# Display records
print("\n -- DISPLAYING STUDENT RECORDS --")
for doc in new_student_list:
    print("\n Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# End of program
input("\n\n End of program, press any key to continue...")