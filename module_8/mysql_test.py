# Written by: Lucas Cheney
# 02/05/2023
# For: CYBR410-T3-1
# ATTN: Professor Haas
# Code for proof of proper DB configuration according to provided requirements.





# Introducing the proper modules to the code for connecting with MySQL server.
import mysql.connector 
from mysql.connector import errorcode

# Username/Password configuration for localhost MySQL instance.
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# db assignment for the connection check
db = mysql.connector.connect(**config)

# Attempt to connect with pysports db
try: 
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")

# If connection fails this tells the program how to display errors to the user.
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

# Closes the db at the end of the connection check.
finally:
    db.close()
