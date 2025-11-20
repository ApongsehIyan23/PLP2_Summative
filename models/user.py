class User:
    """Class to represent a user in the system"""

    def __init__(self, username, password, name, role, industry, bio):
        self.username = username
        self.password = password
        self.name = name
        self.role = "Founder" if role == 1 else "Mentor" if role == 2 else "Investor"
        self.industry = industry
        self.bio = bio