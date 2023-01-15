                    # Title: pytech_insert.py
                    # Written By: Lucas Cheney
                    # For Cyber410-T301 @ Bellevue University
                    # Date: 1/14/2023
                    # Attn: Professor Haas
                    # Description: Program for inserting new documents into the students collection


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

"""three student documents"""
# Rebeka Cheney's document
rebeka = {
    "student_id": "1007",
    "first_name": "Rebeka",
    "last_name": "Cheney",
    "enrollments": [
        {
            "term": "Fall 2022",
            "gpa": "4.0",
            "start_date": "August 21, 2022",
            "end_date": "December 21, 2022",
            "courses": [
                {
                    "course_id": "Science1",
                    "description": "Physical Science",
                    "instructor": "Mrs. Heidinger",
                    "grade": "A+"
                },
                {
                    "course_id": "Art1",
                    "description": "Drawing",
                    "instructor": "Mrs. Biggs",
                    "grade": "A+"
                },
            ]
        }
    ]
}

# Alexis Cheney's document
alexis = {
    "student_id": "1008",
    "first_name": "Alexis",
    "last_name": "Cheney",
    "enrollments": [
        {
            "term": "Fall 2022",
            "gpa": "4.0",
            "start_date": "August 21, 2022",
            "end_date": "December 21, 2022",
            "courses": [
                {
                    "course_id": "Science2",
                    "description": "Biology",
                    "instructor": "Mrs. Heidinger",
                    "grade": "A+"
                },
                {
                    "course_id": "Art1",
                    "description": "Drawing",
                    "instructor": "Mrs. Biggs",
                    "grade": "A+"
                },
            ]
        }    
    ]
}

# Kadey Bates' document
kadey = {
    "student_id": "1009",
    "first_name": "Kadey",
    "last_name": "Bates",
    "enrollments": [
        {
            "term": "Fall 2022",
            "gpa": "4.0",
            "start_date": "August 21, 2022",
            "end_date": "December 21, 2022",
            "courses": [
                {
                    "course_id": "Science3",
                    "description": "Chemistry",
                    "instructor": "Mrs. Heidinger",
                    "grade": "A+"
                },
                {
                    "course_id": "Art2",
                    "description": "Painting",
                    "instructor": "Mrs. Fox",
                    "grade": "A+"
                },
            ]
        }
    ]
}

# Access the students collection
students = db.students

# break before insert/print statements
print("\n -- INSERTED STUDENTS")
# insert and success statements
rebeka_student_id = students.insert_one(rebeka).inserted_id
print(" Rebeka Cheney was inserted into the students collection with document_id" + str(rebeka_student_id))

alexis_student_id = students.insert_one(alexis).inserted_id
print(" Alexis Cheney was inserted into the students collection with document_id" + str(alexis_student_id))

kadey_student_id = students.insert_one(kadey).inserted_id
print(" Kadey Bates was inserted into the students collection with document_id" + str(kadey_student_id))

input("\n\nEnd of program, press any key to exit...")