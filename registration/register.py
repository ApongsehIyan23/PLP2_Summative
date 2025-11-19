import hashlib
import getpass

#code to register users

class User:
    """Class to represent a user in the system"""

    def __init__(self, username, password, name, role, industry, bio):
        self.username = username
        self.password = password
        self.name = name
        self.role = "Founder" if role == 1 else "Mentor" if role == 2 else "Investor"
        self.industry = industry
        self.bio = bio
    

class Founder(User):

    """Class to represent a founder in the Database"""
    def __init__(self, username, password, name, role, industry, bio,
                 startup_name, startup_description, years_of_operation, stage):
         super().__init__(username, password, name, 1 , industry, bio)
         self.startup_name = startup_name
         self.startup_description = startup_description
         self.years_of_operation = years_of_operation
         self.stage = stage
    
    def display_founder_info(self):
        """Display all founder information"""
        print("=" * 60)
        print("FOUNDER PROFILE")
        print("=" * 60)
        print(f"Username: {self.username}")
        print(f"Full Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Industry: {self.industry}")
        print(f"Bio: {self.bio}")
        print("-" * 60)
        print("STARTUP INFORMATION")
        print("-" * 60)
        print(f"Startup Name: {self.startup_name}")
        print(f"Description: {self.startup_description}")
        print(f"Years of Operation: {self.years_of_operation}")
        print(f"Stage: {self.stage}")
        print("=" * 60)


def display_details(username, name, role, industry, bio):
    print("================= USER DETAILS =================")
    role_name = "Founder" if role == 1 else "Mentor" if role == 2 else "Investor"
    print(f"Username: {username}")
    print(f"Name: {name}")
    print(f"Role: {role_name}")
    print(f"Industry: {industry}")
    print(f"Bio: {bio}\n")


def register_user():
    """Function to register a new user"""

    print("=== User Registration ===")
    username = input("Enter Username: ").strip()
    name = input("Enter Full Name: ").strip()
    industry = input("Enter Industry: ").strip()
    bio = input("Enter a short Bio: ").strip()
    
    if not all([username, name, industry, bio]):
        print("ERROR: All fields are required!")
        return None
    
    if not all(c.isalpha() or c.isspace() for c in name):
        print("ERROR: Name must contain only alphabetic characters and spaces.")
        return None
    
    print("=" * 60 + "\n")
    print(f"User: {name}, you're 2 steps closer to creating your Account")
    
    while True:
        try:
            role = int(input("Enter Role (Founder = 1, Mentor = 2, Investor = 3): "))
            if role not in [1, 2, 3]:
                print("ERROR: Role must be 1, 2, or 3")
                continue
            break
        except ValueError:
            print("ERROR: Please enter a valid number")
    
    while True:
        password = getpass.getpass("Create password (min 8 characters): ")
        if len(password) < 8:
            print("ERROR: Password must be at least 8 characters")
            continue
        
        confirm = getpass.getpass("Confirm password: ")
        if password == confirm:
            print("Passwords match!")
            break
        print("Passwords do not match! Try again")
    
    display_details(username, name, role, industry, bio)
    decision = input("Do you want to confirm this data [y/n]: ").strip().lower()
