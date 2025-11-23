"""Package to contain the Menu functions for the logged-in user"""

def start_main_menu(connection, user):
    from welcome import clear_screen
    """Funtion to display the menu and options for the logged in user"""

    #selection based menu
    while True:
        print("\n" + "=" * 30 + " MAIN MENU " + "=" * 30)
        print("1. View Dashboard ")
        print("2. Find & Connect ")
        print("3. Manage Connections ")
        print("4. View Connections ")
        print("5. Logout!")
        try:
            choice = int(input("Enter your Choice ....... >>>>>>>>>> "))
            clear_screen()
            if choice not in range(1,6):
                print("Invalid Choice! Must be between (1 - 5)")
            
            elif choice == 1:
                
                print("viewdashboard_function goes here")

            elif choice == 2:
                print("find&connect function goes here")
                pass
            
            elif choice == 3:
                print("manageconnections function goes here")

            elif choice == 4:
                print("View your connections here")
            
            elif choice == 5:
                from welcome import display_welcome_menu
                #import this function to call take the user back to the menu
                print("Logout Function Selected! ")
                print("Logging out now..............")

                display_welcome_menu(connection)
                return #stop the function execution
        except ValueError as e:
            print(f"Error {e} encountered !. Can't Proceed")
