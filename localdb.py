import sqlite3

# create connection to db file
myconnection = sqlite3.connect("mydb.db")  # Creates a file 'my_database.db'
cursor = myconnection.cursor()
