# Written by: Lucas Cheney
# 02/05/2023
# For: CYBR410-T301
# ATTN: Professor Haas
# Python code for calling to a database.

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
    
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    teams = cursor.fetchall()

    # Print teams from table teams.
    print("\n  -- DISPLAYING TEAM RECORDS --")

    for team in teams:
        print("\n TEAM ID: {}\n TEAM NAME: {}\n MASCOT: {}\n".format(team[0], team[1], team[2]))


    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    players = cursor.fetchall()

    # Print players from table players.
    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    for player in players:
        print("\n PLAYER ID: {}\n FIRST NAME: {}\n LAST NAME: {}\n TEAM ID: {}\n".format(player[0], player[1], player[2], player[3]))

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
