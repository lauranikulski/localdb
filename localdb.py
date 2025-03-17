import sqlite3

# create connection to db file
myconnection = sqlite3.connect("mydb.db")  # Creates a file 'my_database.db'
cursor = myconnection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS films (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        release_year INTEGER NOT NULL,
        rating INTEGER NOT NULL
    )
''')

# Commit changes and close the connection
myconnection.commit()
myconnection.close()