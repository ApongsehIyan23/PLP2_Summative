class User:
    """Class to represent a user in the system"""

    def __init__(self, username, password, name, role, industry, bio):
        self.username = username
        self.password = password
        self.name = name
        self.role = "Founder" if role == 1 else "Mentor" if role == 2 else "Investor"
        self.industry = industry
        self.bio = bio
    
    def get_userID(self, connection):
        """To get the ID of any User: Founder/Mentor/Investor"""

        mycursor = connection.cursor(dictionary=True) #to return a dictionary
        sql_statment = "SELECT user_id FROM users WHERE username = %s"
        val = (self.username,)

        mycursor.execute(sql_statment, val)
        result = mycursor.fetchone()
        mycursor.close()
        return result["user_id"]