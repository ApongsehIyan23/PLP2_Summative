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


    def add_mentor_to_db(self, connection):
        """Add a mentor to the database: the user and mentor tables"""
        
        mycursor = connection.cursor()
        sql_statements = [
            "INSERT INTO users (username, password, name, role, industry, bio) VALUES (%s, %s, %s, %s, %s, %s)",
            """INSERT INTO mentors (user_id, expertise, years_of_experience, availability, previous_mentorships)
             VALUES (%s, %s, %s, %s, %s)"""
        ]
        val = (self.username, self.password, self.name, self.role, self.industry, self.bio)
        try:
            mycursor.execute(sql_statements[0], val) #executing the first insert statement
            user_id = mycursor.lastrowid #to get the id that was just inserted
            
            #inserting into the mentors table
            mycursor.execute(sql_statements[1], (
                user_id, self.expertise, self.years_of_experience, self.availability, self.previous_mentorships
            ))

            connection.commit() #always commit the connection before closing the cursor
            print("\n\n\n")
            print(f"Mentor {self.username} with ID: {user_id} successfully added to the database!")
            mycursor.close()
        except Exception as e:
            print(f"Error {e} encountered, Can't proceed.. Exiting")
            connection.rollback() #undo the changes incase of an error
        pass

    
    @classmethod
    def get_from_db(cls, user_id, connection):
        """Get a mentor from database by user_id"""


        cursor = connection.cursor(dictionary=True)
        
        # Get user data
        cursor.execute('SELECT * FROM users WHERE user_id = %s', (user_id,))
        user_data = cursor.fetchone()
        
        # Get founder-specific data
        cursor.execute('SELECT * FROM mentors WHERE user_id = %s', (user_id,))
        mentor_data = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        return cls(
            username=user_data['username'],
            password=user_data['password'],
            name=user_data['name'],
            role=user_data['role'],
            industry=user_data['industry'],
            bio=user_data['bio'],
            expertise=mentor_data['expertise'],
            years_of_experience=mentor_data['years_of_experience'],
            availability=mentor_data['availability'],
            previous_mentorships=mentor_data['previous_mentorships']
        )