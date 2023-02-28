# Author: Lucas Cheney
# Title: WhatABook Application
# 02/27/2023
# For: CYBR440-T301
# ATTN: Professor Haas

# Import modules
import os
import sys
import mysql.connector
from mysql.connector import errorcode

# DB login configuration
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# Keeps your screen tidy
def cont():
    input("Press any key to continue...")
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

# Prints book DB    
def printbooks():
    cursor.execute("SELECT book_id, book_name, author, details FROM book")
    books = cursor.fetchall()
    for book in books:
        print("\nBook ID: {}\n Title: {}\n Author: {}\n Details: {}".format(book[0], book[1], book[2], book[3]))

# Prints stores DB
def printstores():
    cursor.execute("SELECT store_id, locale FROM store")
    stores = cursor.fetchall()
    for store in stores:
        print("\n Store ID: {}\n Location: {}\n".format(store[0], store[1]))

# Validates user for wishlist interactions
def validuser():
    try:
        uid = int(input("Enter your user ID.\n$"))
        cursor.execute("SELECT * FROM user WHERE user_id = " + str(uid))
        user = cursor.fetchone()
        return user[0]
    except ValueError:
        print("Enter a valid user id.")
        return False
    except TypeError:
        print("Enter a valid user id.")
        return False

# Prints wishlist in list format excluding user data
def printwishlist(user):
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author, book.details FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id WHERE user.user_id =" + str(user))
    wishlist = cursor.fetchall()
    for i in wishlist:
        book = i[3], i[4], i[5], i[6]
        print(book)

# User main menu
def printaccountmain():
    print(" -- Welcome User" + str(user) +" --")
    print("1) Show Wishlist\n2) Show Available Books\n3) Add Book\n4) Remove Book\n5) Main Menu")

# Shows available books not on user's wishlist
def showbooks(user):
    cursor.execute("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = " + str(user)+")")
    books = cursor.fetchall()
    available_books = []
    for book in books:
        available_books.append(book[0])
        print("Book ID: {}\n Title: {}\n Author: {}\n Details: {}".format(book[0], book[1], book[2], book[3]))
    return available_books

# Adds book to user's wishlist
def addbook(user, book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES("+ str(user) + ", " + str(book_id) + ")")
    db.commit()
    print(str(book_id) +" Successfully added to wishlist.")

# Removes books from user's wishlist
def removebook(user, book_id):
    cursor.execute("DELETE FROM wishlist WHERE user_id = "+ str(user) +" AND book_id =" + str(book_id))
    db.commit()
    print(str(book_id) +" Successfully removed from wishlist.")

# Main menu
def mainmenu():
    print(" -- Welcome to WhatABook Main Menu --")
    print("\n1) View Books\n2) Store Locations\n3) Wishlist\n4) Exit")

# Main program
if __name__ == "__main__":
    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        prompt = 0
        while prompt != 4:
            mainmenu()
            try:
                prompt = int(input("$"))
                if prompt > 4 or prompt < 1:
                    raise ValueError
                elif prompt == 1:
                    printbooks()
                    cont()
                elif prompt == 2:
                    printstores()
                    cont()
                elif prompt == 3:
                    validUser = False
                    option = 0
                    goback = "n"
                    while goback.lower() != "y":
                            user = validuser()
                            if user:
                                validUser = True
                            else:
                                quitFromNoUserID = input( "Quit? (y)es or (n)o?\n$")
                                if quitFromNoUserID.lower() == "y":
                                    cont()
                                    sys.exit(2)
                            try:
                                printaccountmain()
                                option = int(input("$"))
                                while goback.lower() != 'y':
                                    if option == 1:
                                        printwishlist(user)
                                        break
                                    elif option == 2:
                                        showbooks(user)
                                        break
                                    elif option == 3:
                                        bookadded = False
                                        while not bookadded:
                                            available_books = showbooks(user)
                                            try:
                                                add_book = int(input("-- Enter the Book ID --\n$"))
                                                if add_book not in available_books:
                                                    print("That book is not available at this time. Choose another.\n$")
                                                    cont()
                                                else: 
                                                    bookadded = True
                                            except ValueError:
                                                print("Please select from the available options.")
                                        addbook(user, add_book)
                                        cont()
                                        break
                                    elif option == 4:
                                        printwishlist(user)
                                        remove_book = int(input("What book would you like to remove?"))    
                                        removebook(user, remove_book)
                                        cont()
                                        break
                                    elif option == 5:
                                        goback = "y"
                            except ValueError:
                                input("Press any ket to continue...")
                elif prompt == 4:
                    cont()
                    sys.exit(2)
            except ValueError:
                print("Please select from the available options.")

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
