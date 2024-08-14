import sqlite3
from sqlite3 import Error

# Function to create a database connection
def create_connection(db_file):
    """
    Create a database connection to a SQLite database specified by db_file.
    If the database does not exist, it will be created.
    """
    connection = None
    try:
        # Attempt to connect to the database file
        connection = sqlite3.connect(db_file)
        print("Connection to SQLite DB successful")
    except Error as e:
        # If there is an error, print it out
        print(f"The error '{e}' occurred")
    
    return connection

# Function to create a table in the database
def create_table(connection):
    """
    Create a table called 'users' if it does not already exist.
    The table has the following columns:
    - id: an integer that auto-increments (primary key)
    - name: a text field for the user's name
    - age: an integer field for the user's age
    - gender: a text field for the user's gender
    """
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      age INTEGER,
      gender TEXT
    );
    """
    try:
        # Create a cursor object to execute SQL commands
        cursor = connection.cursor()
        # Execute the SQL command to create the table
        cursor.execute(create_users_table)
        print("Table created successfully")
    except Error as e:
        # If there is an error, print it out
        print(f"The error '{e}' occurred")

# Function to insert a new user into the 'users' table
def insert_user(connection, user):
    """
    Insert a new user into the 'users' table.
    The 'user' parameter is a tuple containing (name, age, gender).
    """
    insert_user_sql = """
    INSERT INTO
      users (name, age, gender)
    VALUES
      (?, ?, ?);
    """
    try:
        # Create a cursor object to execute SQL commands
        cursor = connection.cursor()
        # Execute the SQL command with the provided user data
        cursor.execute(insert_user_sql, user)
        # Commit the transaction to save changes
        connection.commit()
        print("User added successfully")
    except Error as e:
        # If there is an error, print it out
        print(f"The error '{e}' occurred")

# Function to fetch all users from the 'users' table
def fetch_users(connection):
    """
    Query all rows in the 'users' table and print them.
    Each row represents a user with their id, name, age, and gender.
    """
    try:
        # Create a cursor object to execute SQL commands
        cursor = connection.cursor()
        # Execute the SQL command to select all users
        cursor.execute("SELECT * FROM users")
        # Fetch all rows from the executed command
        rows = cursor.fetchall()
        
        # Iterate through the rows and print each user's information
        for row in rows:
            print(row)
    except Error as e:
        # If there is an error, print it out
        print(f"The error '{e}' occurred")

# Main block to execute the functions
if __name__ == "__main__":
    # Create a connection to the SQLite database file 'users.db'
    connection = create_connection("users.db")
    # Create the 'users' table if it doesn't already exist
    create_table(connection)

    # Loop to allow the user to input multiple users
    while True:
        # Get user input for the new user's details
        name = input("Enter the user's name: ")
        age = int(input("Enter the user's age: "))
        gender = input("Enter the user's gender: ")

        # Insert the user into the database
        insert_user(connection, (name, age, gender))

        # Ask if the user wants to add another record
        another = input("Do you want to add another user? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    # Fetch and print all users from the 'users' table
    fetch_users(connection)
