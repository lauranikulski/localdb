import sqlite3

# create connection to db file
myconnection = sqlite3.connect("mydb.db")  # Creates a file 'my_database.db'

# a cursor like so keeps track of the position in the result set
cursor = myconnection.cursor()

# check for changes 
print(myconnection.total_changes)

if cursor.fetchone() is None: 

# connect to database
    with sqlite3.connect("mydb.db") as myconnection:
        cursor = myconnection.cursor()
    
    # create a table
        cursor.execute('''CREATE TABLE IF NOT EXISTS films (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        release_year INTEGER
                    )''')

    # add entries
        cursor.execute("INSERT INTO films (id, name, release_year) VALUES (?, ?, ?)", 
                (1, "The Matrix", 1999))
        cursor.execute("INSERT INTO films (id, name, release_year) VALUES (?, ?, ?)", 
                (2, "Monster's, Inc.", 2001))

        with sqlite3.connect("mydb.db") as myconnection:
            cursor = myconnection.cursor()
            cursor.execute("SELECT * FROM films")
            rows = cursor.fetchall()
    
            for row in rows:
                print(row)  # Output: (1, 'The Matrix', 1999), (2, "Monster's, Inc.", 2001)
    
    
# Commit changes and close the connection
myconnection.commit()
myconnection.close()