import sqlite3

# check if my record exists
def record_exists(cursor, film_name):
    cursor.execute("SELECT 1 FROM films WHERE name = ?", (film_name,))
    return cursor.fetchone() is not None  # Returns True if a record exists

# Connect to database (automatically closes at the end)
with sqlite3.connect("mydb.db") as myconnection:
    cursor = myconnection.cursor()

    # Create the table if it doesn't exist. AUTOINCREMENT adds index +1 per entry
    cursor.execute('''CREATE TABLE IF NOT EXISTS films (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        name TEXT UNIQUE, 
                        release_year INTEGER
                    )''')

    # records I want to add
    films = [("The Matrix", 1999), ("Monster's, Inc.", 2001)]

    for film in films:
        if not record_exists(cursor, film[0]):  # Only insert if the film is not already in the table
            cursor.execute("INSERT INTO films (name, release_year) VALUES (?, ?)", film)

    # show what's in my database
    cursor.execute("SELECT * FROM films")
    rows = cursor.fetchall()

    for row in rows:
        print(row)  