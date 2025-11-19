from welcome import *
from db_connection import *



if __name__ == "__main__":
    # Initialize the database connection
    db_connection = initialise_database_connection()
    if db_connection:
        display_welcome_screen()
        display_welcome_menu()
        close_database_connection(db_connection)