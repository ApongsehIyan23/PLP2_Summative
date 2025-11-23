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
        print("\n")
        print("=" * 60)
        print("Profile Information")
        print("=" * 60)
        print(f"Username: {self.username}")
        print(f"Full Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Industry: {self.industry}")
        print(f"Bio: {self.bio}")
        print("\n")
        print("-" * 60)
        print("Investor Details ")
        print("-" * 60)
        print(f"Investment Stage: {self.investment_stage}")
        print(f"Investment Range: {self.investment_range}")
        print(f"Investment Record: {self.previous_investments}")
        print("=" * 60)
    

    def add_investor_to_db(self, connection):
        """Add a investor to the database: the user and investor tables"""
        
        mycursor = connection.cursor()
        sql_statements = [
            "INSERT INTO users (username, password, name, role, industry, bio) VALUES (%s, %s, %s, %s, %s, %s)",
            """INSERT INTO investors (user_id, investment_stage, investment_range, previous_investments)
             VALUES (%s, %s, %s, %s)"""
        ]
        val = (self.username, self.password, self.name, self.role, self.industry, self.bio)
        try:
            mycursor.execute(sql_statements[0], val) #executing the first insert statement
            user_id = mycursor.lastrowid #to get the id that was just inserted
            
            #inserting into the investors table
            mycursor.execute(sql_statements[1], (
                user_id, self.investment_stage, self.investment_range, self.previous_investments
            ))

            connection.commit() #always commit the connection before closing the cursor
            print("\n\n\n")
            print(f"Investor {self.name} with ID: {user_id} successfully added to the database!")
            mycursor.close()
        except Exception as e:
            print(f"Error {e} encountered, Can't proceed.. Exiting")
            connection.rollback() #undo the changes incase of an error
        pass

    @classmethod
    def get_from_db(cls, user_id, connection):
        """Get an investor from database by user_id"""


        cursor = connection.cursor(dictionary=True)
        
        # Get user data
        cursor.execute('SELECT * FROM users WHERE user_id = %s', (user_id,))
        user_data = cursor.fetchone()
        
        # Get Investor-specific data
        cursor.execute('SELECT * FROM investors WHERE user_id = %s', (user_id,))
        investor_data = cursor.fetchone()
        
        cursor.close()
        
        return cls(
            username=user_data['username'],
            password=user_data['password'],
            name=user_data['name'],
            role=user_data['role'],
            industry=user_data['industry'],
            bio=user_data['bio'],
            investment_stage=investor_data['investment_stage'],
            investment_range=investor_data['investment_range'],
            previous_investments=investor_data['previous_investments']
        )