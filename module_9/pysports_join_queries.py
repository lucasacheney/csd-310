# Written by: Lucas Cheney
# 02/11/2023
# For: CYBR410-T301
# ATTN: Professor Haas
# Python code for creating a joined table using INNER JOIN method.

# Import connection modules
import mysql.connector
from mysql.connector import errorcode

# Login configuration
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# Assignments used by main code to make call to the db
db = mysql.connector.connect(**config)
cursor = db.cursor()

# Attempt to access db.
try:
    
    # Python execution for creating inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    print("\n -- DISPLAYING RECORDS --")

    # Displays the joined tables
    for player in players:
        print("\n  PLAYER ID: {}\n FIRST NAME: {}\n LAST NAME: {}\n TEAM NAME: {}\n".format(player[0], player[1], player[2], player[3]))

     # Input operator to cause program to hang.
    input("\n Press any key to continue...")

# Code for handling common errors.
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The username/password are invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The database doesn't exist.")

    else:
        print(err)

# Closing connection to db.
finally:
    db.close()