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