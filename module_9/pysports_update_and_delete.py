# Written by: Lucas Cheney
# 02/11/2023
# For: CYBR410-T301
# ATTN: Professor Haas
# Python code for adding and removing player from DB player.

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


# Creates join to show all players
def show_players(cursor, title):
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    print("\n -- {} --".format(title))

    for player in players:
        print("\n PLAYER ID: {}\n FIRST NAME: {}\n LAST NAME: {}\n TEAM NAME: {}\n".format(player[0], player[1], player[2], player[3]))

# Attempt to access db.
try:
    # Insert player
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                "VALUES(%s, %s, %s)")
    
    # New player data
    player_data = ("Smeagol", "Shire Folk", 1)
    cursor.execute(add_player, player_data)
    
    # Commits new data to database
    db.commit()

    # Displays newly inserted data
    show_players(cursor, " DISPLAYING PLAYERS")
 
    # Update records and display new data
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    cursor.execute(update_player)
    db.commit()
    show_players(cursor, "DISPLAYING UPDATED DATA FIELDS")

    # Delete player from player DB and display the data
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")
    cursor.execute(delete_player)
    db.commit()
    show_players(cursor, "DISPLAYING UPDATED DATA FIELDS")

    

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