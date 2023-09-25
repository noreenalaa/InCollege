import sqlite3
# SQLite database setup
# Connect to the SQLite database (creates 'user_data.db' if it doesn't exist)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()  # Create a cursor object to execute SQL commands

# Create a table to store user data if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT,
        firstName TEXT,
        lastName TEXT
    )
''')

# Create a table to store user stories if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS stories (
        story TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        title TEXT,
        description TEXT,
        employer TEXT,
        location TEXT,
        salary TEXT,
        firstname TEXT,
        lastname TEXT
    )
''')

# SQL command to create a 'users' table with 'username' and 'password' columns if it doesn't exist
conn.commit()  # Commit the changes to the database
MAX_ACCOUNTS = 5  # Maximum number of allowed accounts
MAX_JOBS = 5
