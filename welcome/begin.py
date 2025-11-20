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


def display_welcome_menu(connection):
    from registration import register_user # Importing register_user function
    print("=========================================")
    print("1. Register User")
    print("2. Login")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice >>>> "))

        if choice == 1:
            register_user(connection)
        elif choice == 2:
            print("Login function here")
            #login_user()
        elif choice == 3:
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

    except ValueError:
        print("Enter a valid integer!")
