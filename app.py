import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("simple_app.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create a 'users' table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT
)
''')

# Function to add a user to the database
def add_user(name, age, gender):
    cursor.execute("INSERT INTO users (name, age, gender) VALUES (?, ?, ?)", (name, age, gender))
    connection.commit()
    print("User added successfully")

# Function to fetch and display all users
def fetch_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)

# Main program
if __name__ == "__main__":
    while True:
        name = input("Enter the user's name: ")
        age = int(input("Enter the user's age: "))
        gender = input("Enter the user's gender: ")
        
        add_user(name, age, gender)
        
        another = input("Do you want to add another user? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    print("\nAll users in the database:")
    fetch_users()

    # Close the database connection
    connection.close()
