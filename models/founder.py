from .user import *

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
    
    def add_founder_to_db(self, connection):
        """Add a founder to the database: the user and founder tables"""
        
        mycursor = connection.cursor()
        sql_statements = [
            "INSERT INTO users (username, password, name, role, industry, bio) VALUES (%s, %s, %s, %s, %s, %s)",
            """INSERT INTO founders (user_id, startup_name, startup_description, years_of_operation, stage)
             VALUES (%s, %s, %s, %s, %s)"""
        ]
        val = (self.username, self.password, self.name, self.role, self.industry, self.bio)
        try:
            mycursor.execute(sql_statements[0], val) #executing the first insert statement
            user_id = mycursor.lastrowid #to get the id that was just inserted
            
            #inserting into the founders table
            mycursor.execute(sql_statements[1], (
                user_id, self.startup_name, self.startup_description, self.years_of_operation, self.stage
            ))

            connection.commit() #always commit the connection before closing the cursor
            print("\n\n\n")
            print(f"Founder {self.username} with ID: {user_id} successfully added to the database!")
            mycursor.close()
        except Exception as e:
            print(f"Error {e} encountered, Can't proceed.. Exiting")
            connection.rollback() #undo the changes incase of an error
        pass

    @classmethod
    def get_from_db(cls, user_id, connection):
        """Get a founder from database by user_id"""


        cursor = connection.cursor(dictionary=True)
        
        # Get user data
        cursor.execute('SELECT * FROM users WHERE user_id = %s', (user_id,))
        user_data = cursor.fetchone()
        
        # Get founder-specific data
        cursor.execute('SELECT * FROM founders WHERE user_id = %s', (user_id,))
        founder_data = cursor.fetchone()
        
        cursor.close()
        
        return cls(
            username=user_data['username'],
            password=user_data['password'],
            name=user_data['name'],
            role=user_data['role'],
            industry=user_data['industry'],
            bio=user_data['bio'],
            startup_name=founder_data['startup_name'],
            startup_description=founder_data['startup_description'],
            years_of_operation=founder_data['years_of_operation'],
            stage=founder_data['stage']
        )