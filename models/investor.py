from .user import *

class Investor(User):

    """Class to represent an Investor in the Database"""
    def __init__(self, username, password, name, role, industry, bio,
                 investment_stage, investment_range, previous_investments):
        super().__init__(username, password, name, 3 , industry, bio)
        self.investment_stage = investment_stage
        self.investment_range = investment_range
        self.previous_investments = previous_investments

    def display_investor_info(self):
        """Display all Investor information"""
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
        print("Investor Details ")
        print("-" * 60)
        print(f"Investment Stage: {self.investment_stage}")
        print(f"Investment Range: {self.investment_range}")
        print(f"Investment Record: {self.previous_investments}")
        print("=" * 60)