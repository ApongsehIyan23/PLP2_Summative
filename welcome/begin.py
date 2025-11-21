def display_welcome_screen():
    """Display welcome screen with ASCII art"""
    
    print("\n" * 2)  # Add some space at top
    
    print("_" * 50)
    print("=" + " " * 48 + "=")
    print("=" + " " * 10 + "WELCOME TO STARTUP CONNECT" + " " * 12 + "=")
    print("=" + " " * 48 + "=")
    print("=" + " " * 5 + "Connecting Rwandan Founders, Mentors &" + " " * 13 + "=")
    print("=" + " " * 12 + "Investors Together" + " " * 18 + "=")
    print("=" + " " * 48 + "=")
    print("=" * 50)
    
    print("\n")
    input("Press Enter to continue...")  # ← This pauses until user presses Enter
    print("\n")


def check_if_tables_exists(connection):
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    cursor.close()

    return len(tables) > 0

def display_welcome_menu(connection):
    from registration import register_user # Importing register_user function
    from login import login_user # importing the login user function

    print("=========================================")
    print("1. Register User")
    print("2. Login")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice >>>> "))

        if choice == 1:
            register_user(connection)
        elif choice == 2:
            print("\n\n\n")
            print("=================== LOGIN SECTION =====================")
            status = check_if_tables_exists(connection)
            if status == 0:
                print("CAN'T LOGIN BECAUSE THE DATABASE IS EMPTY!!!")
                exit()
            import getpass
            session_username = input("Enter your Username: ")
            session_password = getpass.getpass("Enter your Password: ")

            while not all([session_username, session_password]):
                print("ERROR: All fields are required!")

                session_username = input("Enter your Username: ")
                session_password = getpass.getpass("Enter your Password: ")
            
            new_user = login_user(session_username, session_password, connection) #try to login with the credentials

            if new_user: #if a User was found
                print(f"Welcome Back Dear {new_user.name}! ")
                print(f"Nice to have you back on our Startup Connect!")
            
            else: #if no user was found
                print(f"Invalid Credentials, couldn't retrieve UserName {session_username} from the Database!")

        elif choice == 3:
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

    except ValueError:
        print("Enter a valid integer!")
