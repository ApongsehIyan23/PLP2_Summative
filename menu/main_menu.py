"""Package to contain the Menu functions for the logged-in user"""

def start_main_menu(connection, user, userid):
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
                if user.role == "Founder":
                    user.display_founder_info()
                elif user.role == "Mentor":
                    user.display_mentor_info()
                else:
                    user.display_investor_info()
                
                stats = user.get_stats(userid, connection) #to get the user's statistics
    
                print(f"\nStatistics:")
                print(f"----------")
                print(f"Total Connections: {stats['connections']}")
                print(f"Pending Requests (Received): {stats['pending_received']}")
                print(f"Pending Requests (Sent): {stats['pending_sent']}")
                print("="*50)
            

            elif choice == 2:
                
                while True:    # ← submenu loop
                    print("find&connect function goes here")
                    print(f"1. Browse All Users in {user.industry}")
                    print("2. Browse User By Name ")
                    print("3. Return to Main Menu ")

                    try:
                        submenu_choice = int(input("Enter your Choice .......... >>>>>>>>>> "))

                        if submenu_choice not in range(1,4):
                            print("Invalid Choice... Try again!")

                        elif submenu_choice == 1:
                            print(f"Displaying All Profiles in the {user.industry}")
                            # run function here
                            user.find_matching_profiles(userid, connection)
                            input("\nPress ENTER to return to the Main Menu...")
                            break   # ← returns to MAIN MENU
                
                        elif submenu_choice == 2:
                            print("Enter a name to search for")
                            # run function here
                            input("\nPress ENTER to return to the Main Menu...")
                            break   # ← returns to MAIN MENU

                        elif submenu_choice == 3:
                            break  # ← returns to MAIN MENU

                    except ValueError as e:
                        print(f"Error: {e}")
                
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
