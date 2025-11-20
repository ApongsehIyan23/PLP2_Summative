from .user import *

class Mentor(User):

    """Class to represent a mentor in the Database"""
    def __init__(self, username, password, name, role, industry, bio,
                 expertise, years_of_experience, availability, previous_mentorships):
        super().__init__(username, password, name, 2 , industry, bio)
        self.expertise = expertise
        self.years_of_experience = years_of_experience
        self.availability = availability
        self.previous_mentorships = previous_mentorships
    
    def display_mentor_info(self):
        """Display all Mentor information"""
        print("\n\n\n")
        print("=" * 60)
        print("Profile Information")
        print("=" * 60)
        print(f"Username: {self.username}")
        print(f"Full Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Industry: {self.industry}")
        print(f"Bio: {self.bio}")
        print("\n\n\n")
        print("-" * 60)
        print("Mentor Details ")
        print("-" * 60)
        print(f"Expertise: {self.expertise}")
        print(f"Years of Experience: {self.years_of_experience}")
        print(f"Availability: {self.availability}")
        print(f"Previous Mentorships: {self.previous_mentorships}")
        print("=" * 60)
