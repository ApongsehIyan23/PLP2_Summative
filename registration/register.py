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
    
    
    if decision == 'y' and role == 1: #The User is a Founder
        print("Founder Registration Progress: 50%!")
        print(f"WARNING!: User {username}, hasn't been INSERTED into the DATABASE. ")
        print(f"In order to complete the process, please fill the information below! ")

        venture_name = input("Enter your Startup: >>>>>>> ").strip()
        description = input("Enter the Description: >>>>>> ").strip()


        if not venture_name or not description:
            print("ERROR: Both Startup Name and Description are REQUIRED!!")
            return None

        if not any(c.isalpha() for c in venture_name) or len(venture_name) < 2:
            print("ERROR: Startup Name must be at least 2 characters and contain letters!")
            return None

        if not any(c.isalpha() for c in description) or len(description) < 10:
            print("ERROR: Description must be at least 10 characters and contain letters!")
            return None

        while True:
            try:
                stage = int(input(
                    "Select your startup stage:\n"
                    "1: Idea\n"
                    "2: Early\n"
                    "3: Growth\n"
                    "4: Established\n"
                    "Enter option (1 - 4): "
                ))
                yr_operation = int(input(
                    "Select the years of operation:\n"
                    "1: Less than 1 year\n"
                    "2: 1 - 2 years\n"
                    "3: 3 - 5 years\n"
                    "4: 5 years+\n"
                    "Enter option (1 - 4): "
                ))
                if yr_operation not in [1, 2, 3, 4] or stage not in [1, 2, 3, 4]:
                    print("Error: Both Options must be between 1 - 4")
                    continue
                break
            except ValueError:
                print("Please Enter a Valid Number ! ")

        #creating the founder class
        STAGES = {1: "Idea", 2: "Early", 3: "Growth", 4: "Established"}
        YEARS = {1: "Less than 1 year", 2: "1-2 years", 3: "3-5 years", 4: "5+ years"}
        
        # Create the Founder object
        founder = Founder(username, hashlib.sha256(password.encode()).hexdigest(), name, 1, industry, bio, venture_name, description,
            YEARS[yr_operation],
            STAGES[stage]
        )

        founder.display_founder_info()