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

