from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for declarative models
Base = declarative_base()

# Define the User class which maps to the 'users' table in the database
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String)

# Function to create a database engine and session
def get_engine_and_session(db_name="users.db"):
    """
    Create a database engine and a session to interact with the SQLite database.
    """
    engine = create_engine(f'sqlite:///{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()
    return engine, session

# Function to create the users table
def create_table(engine):
    """
    Create the users table in the database if it doesn't exist.
    """
    Base.metadata.create_all(engine)
    print("Table created successfully")

# Function to add a new user to the database
def add_user(session, name, age, gender):
    """
    Add a new user to the database.
    """
    user = User(name=name, age=age, gender=gender)
    session.add(user)
    session.commit()
    print("User added successfully")

# Function to fetch and print all users from the database
def fetch_users(session):
    """
    Fetch all users from the database and print their details.
    """
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}, Gender: {user.gender}")

# Main block to execute the functions
if __name__ == "__main__":
    # Create the database engine and session
    engine, session = get_engine_and_session()

    # Create the users table if it doesn't already exist
    create_table(engine)

    # Loop to allow the user to input multiple users
    while True:
        # Get user input for the new user's details
        name = input("Enter the user's name: ")
        age = int(input("Enter the user's age: "))
        gender = input("Enter the user's gender: ")

        # Add the user to the database
        add_user(session, name, age, gender)

        # Ask if the user wants to add another record
        another = input("Do you want to add another user? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    # Fetch and print all users from the 'users' table
    fetch_users(session)
