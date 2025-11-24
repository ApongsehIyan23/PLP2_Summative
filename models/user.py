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
    
    def get_stats(self, ID, connection):
        "To get connection statistics of each User"

        mycursor = connection.cursor()

        # Count connections
        mycursor.execute('''
            SELECT COUNT(*) as count FROM connections
            WHERE (sender_id = %s OR receiver_id = %s) AND status = 'accepted'
        ''', (ID, ID))
        connections_count = mycursor.fetchone()[0]
        
        # Count pending received
        mycursor.execute('''
            SELECT COUNT(*) as count FROM connections
            WHERE receiver_id = %s AND status = 'pending'
        ''', (ID,))
        pending_received = mycursor.fetchone()[0]
        
        # Count pending sent
        mycursor.execute('''
            SELECT COUNT(*) as count FROM connections
            WHERE sender_id = %s AND status = 'pending'
        ''', (ID,))
        pending_sent = mycursor.fetchone()[0]
        
        mycursor.close()
        
        return {
            'connections': connections_count,
            'pending_received': pending_received,
            'pending_sent': pending_sent
        }
    
    def find_matching_profiles(self, ID, connection):
        """Method to find the matching Profiles based on the Industry for any User Object"""
        from tabulate import tabulate #import tabulate to display results in tabular format
        mycursor = connection.cursor(dictionary=True)

        mycursor.execute(
            "SELECT name, role, bio FROM users WHERE (user_id != %s AND industry = %s)"
            ,(ID, self.industry)
        )

        profile_matches = mycursor.fetchall()
        mycursor.close()

        if not profile_matches:
            print(f"No profiles found in the {self.industry} industry.")
        else:
            # Prepare data for tabulate
            table_data = []
            for profile in profile_matches:
                table_data.append([profile['name'], profile['role'], profile['bio']])
        
            print(tabulate(table_data, headers=["Name", "Role", "Bio"], tablefmt="fancy_grid"))
