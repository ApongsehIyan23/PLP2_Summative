"""
Package for database connection initialization.
This module sets up the database connection and initializes the database. """

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), "credentials.env") #computing where the env file is located
load_dotenv(dotenv_path)

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT", 3306))  # default port 3306 if not specified
def initialise_database_connection():
    try:
        global connection 
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT
        )
        if connection.is_connected():
            print("Database Connection Established with no Errors............!")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def close_database_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Database connection closed.")
    else:
        print("Connection was already closed or not established.")


def create_all_tables():
        if connection is None: return
        cursor = connection.cursor()
        tables = {
    "users": """
        CREATE TABLE IF NOT EXISTS users (
            user_id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(255) UNIQUE NOT NULL,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            role ENUM('Founder', 'Mentor', 'Investor') NOT NULL,
            industry TEXT NOT NULL,
            bio TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB;
    """,

    "founders": """
        CREATE TABLE IF NOT EXISTS founders (
            founder_id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT UNIQUE NOT NULL,
            startup_name TEXT NOT NULL,
            startup_description TEXT,
            years_of_operation ENUM('Less than 1 year', '1-2 years', '3-5 years', '5+ years'),
            stage ENUM('Idea', 'Early', 'Growth', 'Established'),
            
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        ) ENGINE=InnoDB;
    """,

    "mentors": """
        CREATE TABLE IF NOT EXISTS mentors (
            mentor_id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT UNIQUE NOT NULL,
            expertise TEXT NOT NULL,
            years_of_experience ENUM('0-5 years', '5-10 years', '10-20 years', '20+ years'),
            availability ENUM('5-10 hours/week', '10-20 hours/week', '20+ hours/week'),
            previous_mentorships ENUM('0-5', '5-10', '10-20', '20+'),
            
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        ) ENGINE=InnoDB;
    """,

    "investors": """
        CREATE TABLE IF NOT EXISTS investors (
            investor_id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT UNIQUE NOT NULL,
            investment_stage ENUM('Idea', 'Early', 'Growth', 'Established'),
            investment_range ENUM('1k-5k', '5k-10k', '10k+'),
            previous_investments ENUM('0-5', '5-10', '10-20', '20+'),
            
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        ) ENGINE=InnoDB;
    """,

    "connections": """
        CREATE TABLE IF NOT EXISTS connections (
            connection_id INT PRIMARY KEY AUTO_INCREMENT,
            sender_id INT NOT NULL,
            receiver_id INT NOT NULL,
            status ENUM('Pending', 'Accepted', 'Declined'),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            
            FOREIGN KEY (sender_id) REFERENCES users(user_id) ON DELETE CASCADE,
            FOREIGN KEY (receiver_id) REFERENCES users(user_id) ON DELETE CASCADE,
            
            UNIQUE(sender_id, receiver_id),
            CHECK (sender_id != receiver_id)
        ) ENGINE=InnoDB;
    """
}
        for name, query in tables.items():
            try:
                cursor.execute(query)
                #print(f"Table '{name}' created successfully!")
            except Error as e:
                print(f"Error creating table {name}: {e}")
                print(f"Failed to create ALL TABLES, Hence Program will not work as intended")
                connection.rollback()
                exit()
        connection.commit()
        cursor.close()
