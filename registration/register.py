import hashlib
import getpass

from models.founder import *
from models.mentor import *
from models.investor import *

#code to register users


    




def display_details(username, name, role, industry, bio):
    print("================= USER DETAILS =================")
    role_name = "Founder" if role == 1 else "Mentor" if role == 2 else "Investor"
    print(f"Username: {username}")
    print(f"Name: {name}")
    print(f"Role: {role_name}")
    print(f"Industry: {industry}")
    print(f"Bio: {bio}\n")


def register_user(connection):
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
        """Additional Founder Data Collection and Validation"""
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

        #creating the founder object
        STAGES = {1: "Idea", 2: "Early", 3: "Growth", 4: "Established"}
        YEARS = {1: "Less than 1 year", 2: "1-2 years", 3: "3-5 years", 4: "5+ years"}
        
        # Create the Founder object
        session_founder = Founder(username, hashlib.sha256(password.encode()).hexdigest(), 
                          name, 1, industry, bio, venture_name, description,YEARS[yr_operation], STAGES[stage])

        """Display Founder information and add the founder to the database"""
        session_founder.display_founder_info()
        session_founder.add_founder_to_db(connection)

    elif decision == 'y' and role == 2: #Mentor
        """Additional Mentor Data Collection and Validation"""
        print("Mentor Registration Progress: 50%!")
        print(f"WARNING!: User {username}, hasn't been INSERTED into the DATABASE. ")
        print(f"In order to complete the process, please fill the information below! ")

        expertise = input("Enter your expertise (skilled domain): >>>>>>> ").strip()
        if not expertise:
            print("ERROR: Expertise fiedl is REQUIRED!!")
            return None

        if not any(c.isalpha() for c in expertise) or len(expertise) < 10:
            print("ERROR: Experise must be at least 10 characters and contain letters!")
            return None
        

        while True:
            try:
                yr_experience = int(input(
                    "Select your years of experience:\n"
                    "1: 0 - 5 years\n"
                    "2: 5 - 10 years\n"
                    "3: 10 - 20 years\n"
                    "4: 20 years+\n"
                    "Enter option (1 - 4): "
                ))
                availability = int(input(
                    "Select your availability:\n"
                    "1: 5 - 10 hours/week\n"
                    "2: 10 - 20 hours/week\n"
                    "3: 20+ hours/week\n"
                    "Enter option (1 - 3): "
                ))
                number_mentees = int(input(
                    "How many people have you mentored:\n"
                    "1: 0 - 5\n"
                    "2: 5 - 10\n"
                    "3: 10 - 20\n"
                    "4: 20+\n"
                    "Enter option (1 - 3): "
                ))
                if yr_experience not in [1, 2, 3, 4] or availability not in [1, 2, 3] or number_mentees not in [1, 2, 3, 4]:
                    print("Error: Experience must be between (1 - 4), and Availability must be " \
                    "between (1 - 3). Number of Mentees must be between (1 - 4)!")
                    continue
                break
            except ValueError:
                print("Please Enter a Valid Number ! ")

        #creating the mentor object
        experience = {1: "0-5 years", 2: "5-10 years", 3: "10-20 years", 4: "20+ years"}
        schedule = {1: "5-10 hours/week", 2: "10-15 hours/week", 3: "15-20 hours/week", 4: "20+ hours/week"}
        mentees = {1: "0-5", 2: "5-10", 3: "10-20", 4: "20+"}

        # Create the Mentor object
        session_mentor = Mentor(username, hashlib.sha256(password.encode()).hexdigest(), 
                          name, 1, industry, bio, expertise, experience[yr_experience], schedule[availability], mentees[number_mentees])

        """Display Mentor information and add the mentor to the database"""
        session_mentor.display_mentor_info()
        session_mentor.add_mentor_to_db(connection)
        pass
    elif decision == 'y' and role == 3: #Investor
        pass
    
    else:
        print("Registration cancelled")
        return None